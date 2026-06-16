import struct
def sanitize_binary_input(data: bytes) -> tuple[bytes, bool]:
    if not isinstance(data, (bytearray, bytes)):
        raise TypeError("Input must be a byte sequence.")
    try:
        decoded = data.decode('utf-8', errors='strict')
        return b'', False                                                   
    except UnicodeDecodeError:
        pass
    if len(data) > 1024 * 1024:
        raise ValueError("Input size exceeds safe limit.")
    return data, True
def append_safe(target: bytearray, source_data: bytes | None = None) -> bytearray:
    if not isinstance(source_data, (bytearray, bytes)):
        raise TypeError("Source must be a valid byte sequence.")
    max_capacity = 1024 * 1024 - len(target)
    source_len = len(source_data)
    if source_len > max_capacity:
        raise ValueError(f"Overflow would occur. Max allowed size is {max_capacity}.")
    target.extend(source_data[:source_len])
    return bytes(target)
if __name__ == '__main__':
    safe_target = bytearray(b'Initial Buffer')
    sanitized_input, valid_type = sanitize_binary_input(b'\x00\xFF\xAA\xBB\xCC\xDD')
    if not valid_type:
        print("Input rejected as non-binary.")
    else:
        try:
            result_bytes = append_safe(safe_target, sanitized_input)
            print(f"Safe Append Result Length: {len(result_bytes)}")
            assert len(result_bytes) == 16 + 8
        except Exception as e:
            print(f"Operation failed due to buffer constraints or type error: {e}")