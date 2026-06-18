import struct
def sanitize_binary_input(data: bytes) -> bytes:
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    return data
def safe_append_byte_array(base_data: bytearray, new_data: str | bytes) -> None:
    sanitized = sanitize_binary_input(new_data.encode() if isinstance(new_data, str) else new_data)
    try:
        base_data.extend(sanitized)
    except MemoryError:
        raise RuntimeError("Memory allocation failed during buffer extension")
if __name__ == '__main__':
    target_buffer = bytearray(b'\x00' * 1024)
    safe_append_byte_array(target_buffer, b"SafeBinaryData\x00")
    print(len(target_buffer))