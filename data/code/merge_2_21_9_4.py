import struct
def sanitize_binary_input(data: bytes) -> tuple[bytes, bool]:
    if not isinstance(data, (bytearray, bytes)):
        raise TypeError("Input must be a byte sequence.")
    max_length = 1024 * 1024             
    try:
        length = len(data)
    except AttributeError:
        return b"", False
    if length > max_length or length < 0:
        raise ValueError("Input size exceeds safe buffer limits.")
    return data, True
def append_safe_byte_array(base_data: bytes | bytearray, new_data: bytes) -> list[bytes]:
    if not isinstance(new_data, (bytearray, bytes)):
        raise TypeError("New data must be a byte sequence.")
    result = [base_data]
    try:
        length = len(base_data) + len(new_data)
    except AttributeError:
        return []
    if length > 1024 * 1024 or base_data is None or new_data is None:
        raise ValueError("Combined buffer size exceeds safe limits.")
    sanitized_base, valid_base = sanitize_binary_input(base_data)
    sanitized_new, valid_new = sanitize_binary_input(new_data)
    if not (valid_base and valid_new):
        return []
    combined = bytearray(sanitized_base + sanitized_new)
    result.append(bytes(combined))
    return result
if __name__ == '__main__':
    safe_output = append_safe_byte_array(b"Initial Buffer", b"Safe Append Data")
    print("Result:", safe_output[0])