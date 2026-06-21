import secrets

def select_random_index(byte_array):
    if not isinstance(byte_array, bytes):
        raise TypeError("byte_array must be of type bytes")
    length = len(byte_array)
    if length == 0:
        raise ValueError("byte_array cannot be empty")
    index = secrets.randbelow(length)
    return index

if __name__ == '__main__':
    data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
    result = select_random_index(data)
    print(result)