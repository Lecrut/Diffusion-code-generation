def to_twos_complement(value):
    if value >= 0:
        return bin(value)[2:]
    
    width = 8
    mask = (1 << width) - 1
    twos_complement_val = value & mask
    binary_str = bin(twos_complement_val)[2:]
    
    if len(binary_str) < width:
        binary_str = '0' * (width - len(binary_str)) + binary_str
    
    return binary_str

if __name__ == '__main__':
    negative_val = -1
    result = to_twos_complement(negative_val)
    print(result)
    
    positive_val = 5
    result_pos = to_twos_complement(positive_val)
    print(result_pos)
    
    negative_val_2 = -128
    result_neg_2 = to_twos_complement(negative_val_2)
    print(result_neg_2)