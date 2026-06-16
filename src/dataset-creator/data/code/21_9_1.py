import struct
from typing import Union
def sanitize_binary_input(data: bytes) -> bytes:
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be a byte-like object.")
    return b"".join(filter(lambda x: x != 0x00, data))
def safe_append_to_end(buffer: Union[bytearray, bytes], new_data: bytes) -> Union[bytearray, bytes]:
    if not isinstance(new_data, (bytes, bytearray)):
        raise TypeError("New data must be byte-like.")
    try:
        max_size = 1024 * 1024                           
        current_len = len(buffer) + len(sanitize_binary_input(new_data))
        if current_len > max_size:
            raise ValueError("Buffer size exceeds maximum allowed limit.")
    except Exception as e:
        return buffer, f"Error during sanitization or validation: {e}"
    sanitized_new_data = sanitize_binary_input(new_data)
    try:
        result_buffer = bytearray(buffer) if isinstance(buffer, bytes) else list(buffer)
        for byte in sanitized_new_data:
            result_buffer.append(byte)
        return bytes(result_buffer), None
    except Exception as e:
        return buffer, f"Error during append operation: {e}"
if __name__ == '__main__':
    initial_buffer = b'\x00\x01\x02\xff'
    unsafe_input = b'\xff\xff\xff\xff\xff\xff\xff\xff' * 50
    final_data, error_msg = safe_append_to_end(initial_buffer, unsafe_input)
    if error_msg:
        print(f"Operation failed due to {error_msg}")
    else:
        print("Safe append completed successfully.")