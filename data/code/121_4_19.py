def compare_binary_sizes(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b:
        return a
    elif size_b > size_a:
        return b
    else:
        return a

if __name__ == '__main__':
    binary1 = b'\x00\x01\x02'
    binary2 = b'\x00\x01'
    print(compare_binary_sizes(binary1, binary2))
    
    binary3 = b'\x00\x01\x02\x03'
    binary4 = b'\x00\x01\x02'
    print(compare_binary_sizes(binary3, binary4))
    
    binary5 = b'\x00\x01\x02\x03'
    binary6 = b'\x00\x01\x02\x03'
    print(compare_binary_sizes(binary5, binary6))