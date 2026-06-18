import struct
def sanitize_binary_input(data: bytes) -> tuple[bytes, bool]:
    if not isinstance(data, (bytearray, bytes)):
        raise TypeError("Input must be a byte-like object.")
    try:
        max_length = 1024 * 1024                        
        return data, len(data) <= max_length
    except Exception as e:
        print(f"Sanitization error: {e}")
        raise
def safe_append_to_buffer(buffer: bytearray, new_data: bytes) -> None:
    is_safe, length = sanitize_binary_input(new_data)
    if not is_safe or len(buffer) + length > 1048576:
        raise ValueError("Buffer overflow prevention failed.")
    buffer.extend(new_data)
if __name__ == '__main__':
    safe_buffer = bytearray(1024)
    test_input = b'\x00\x01\x02' * 50
    try:
        safe_append_to_buffer(safe_buffer, test_input)
        print("Buffer updated successfully.")
        expected_len = len(test_input) + len(safe_buffer) - 1024
        if len(safe_buffer) == expected_len:
            print(f"Data appended correctly. Total size: {len(safe_buffer)} bytes.")
    except ValueError as e:
        print(f"Security violation detected: {e}")