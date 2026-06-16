import struct
from typing import Union
def sanitize_binary_input(data: bytes) -> bytes:
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be a byte-like object")
    max_length = 1024 * 1024                                                  
    try:
        length = len(data)
    except AttributeError:
        raise ValueError("Invalid input type for length calculation")
    if length > max_length or length < 0:
        raise ValueError(f"Data size {length} exceeds maximum allowed size of {max_length}")
    sanitized = data.rstrip(b'\x00')
    return sanitized
def safe_append_to_end(buffer: bytearray, new_data: Union[bytes, str]) -> None:
    if not isinstance(buffer, bytearray):
        raise TypeError("Buffer must be a bytearray")
    data_to_append = new_data
    if isinstance(data_to_append, str):
        try:
            encoded_bytes = data_to_append.encode('utf-8')
        except UnicodeEncodeError as e:
            raise ValueError(f"Invalid UTF-8 string provided: {e}") from e
        sanitized_encoded = sanitize_binary_input(encoded_bytes)
    else:
        if not isinstance(data_to_append, bytes):
            raise TypeError("Input must be a byte-like object")
        sanitized_data = sanitize_binary_input(data_to_append)
    try:
        buffer.extend(sanitized_data)
    except MemoryError:
        raise RuntimeError("Memory allocation failed during append operation")
if __name__ == '__main__':
    initial_buffer = bytearray(b'\x00\x01\x02')
    safe_payload_1 = b'Hello, World!' + b'\xff\xff\xff'                                     
    unsafe_string_input = "Test Data \x80"                                         
    try:
        safe_append_to_end(initial_buffer, safe_payload_1)
        sanitized_string = sanitize_binary_input(unsafe_string_input.encode('utf-8', errors='ignore'))
        safe_append_to_end(initial_buffer, sanitized_string)
    except Exception as e:
        print(f"Error occurred during sanitization or appending: {e}")
    result = bytes(initial_buffer)
    if len(result) > 0 and all(b == 0 for b in result):
        print("Buffer contains only nulls")
    else:
        print(f"Final Buffer Content (Hex): {result.hex()}")