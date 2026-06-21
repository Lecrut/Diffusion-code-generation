import secrets

def get_secure_random_index(byte_array):
    if not byte_array:
        raise ValueError("byte_array must not be empty")
    max_index = len(byte_array) - 1
    random_index = secrets.randbelow(max_index + 1)
    return random_index

if __name__ == '__main__':
    sample_data = bytes([10, 20, 30, 40, 50, 60, 70, 80])
    result = get_secure_random_index(sample_data)
    print(result)
    print(sample_data[result])