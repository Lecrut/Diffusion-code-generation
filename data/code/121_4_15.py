def compare_binary_sizes(a, b):
    if not isinstance(a, bytes) or not isinstance(b, bytes):
        raise ValueError("Both arguments must be of type bytes")
    
    return a if len(a) > len(b) else b

if __name__ == '__main__':
    binary1 = b'\x01\x02\x03'
    binary2 = b'\x04\x05'
    print(compare_binary_sizes(binary1, binary2))
    
    binary3 = b'\x06\x07\x08\x09'
    binary4 = b'\x0a\x0b\x0c\x0d\x0e'
    print(compare_binary_sizes(binary3, binary4))