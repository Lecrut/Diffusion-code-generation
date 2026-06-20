def compare_binary_sizes(a, b):
    return a if len(a) > len(b) else b

if __name__ == '__main__':
    binary1 = b'\x00\x01\x02\x03'
    binary2 = b'\x04\x05\x06'
    print(compare_binary_sizes(binary1, binary2))
    
    binary3 = b'\x07\x08'
    binary4 = b'\x09\x0a\x0b\x0c'
    print(compare_binary_sizes(binary3, binary4))
    
    binary5 = b''
    binary6 = b'\x0d'
    print(compare_binary_sizes(binary5, binary6))