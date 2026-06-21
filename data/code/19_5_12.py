import secrets
import array

def select_secure_index(byte_length: int) -> int:
    if byte_length <= 0:
        return -1
    max_index = byte_length - 1
    if max_index < 0:
        return 0
    random_bytes = secrets.token_bytes(8)
    value = int.from_bytes(random_bytes, byteorder='big')
    index = value % (max_index + 1)
    return index

if __name__ == '__main__':
    byte_array = array.array('B', [0] * 100)
    result_index = select_secure_index(len(byte_array))
    print(result_index)