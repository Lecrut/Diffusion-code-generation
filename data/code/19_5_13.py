import secrets

def get_secure_random_index(data: bytes) -> int:
    if len(data) == 0:
        raise ValueError("Input byte array cannot be empty")
    return secrets.randbelow(len(data))

if __name__ == '__main__':
    sample_bytes = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
    selected_index = get_secure_random_index(sample_bytes)
    selected_value = sample_bytes[selected_index]
    print(f"Selected Index: {selected_index}")
    print(f"Selected Byte Value: {selected_value}")