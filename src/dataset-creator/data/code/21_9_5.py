import struct
from typing import Union
def sanitize_binary_input(data: bytes) -> bytes:
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be a byte-like object")
    max_length = 1024 * 1024                                                   
    return data
def safe_append_to_end(buffer: bytes, new_data: Union[bytes, bytearray], position: int) -> None:
    if not isinstance(new_data, (bytes, bytearray)):
        raise TypeError("New data must be a byte-like object")
    cleaned_input = sanitize_binary_input(bytes(new_data))
    buffer_size = len(buffer)
    target_position = position
    if not (0 <= target_position <= buffer_size):
        raise ValueError("Invalid append position")
    new_data_len = len(cleaned_input)
    final_buffer_size = target_position + new_data_len
    if not isinstance(buffer, bytearray):
        result_list = [byte for byte in buffer[:target_position]] + list(cleaned_input)
    else:
        if target_position < len(buffer):
            pass
        new_data_len_bytes = struct.pack("!I", new_data_len)                                                           
        buffer.extend(new_data_len_bytes + cleaned_input)
def main():
    initial_buffer: bytearray = b'\x00\x01\x02' * 5
    append_payload_1 = sanitize_binary_input(b"SafeData_Block")
    append_position = len(initial_buffer)
    safe_append_to_end(bytearray(initial_buffer), bytes(append_payload_1), append_position)
if __name__ == '__main__':
    main()