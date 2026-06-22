def compare_lengths(len1, len2):
    is_equal = (len1 == len2)
    is_len1_greater = (len1 > len2)
    
    result = 'equal' if is_equal else ('len1 is greater' if is_len1_greater else 'len2 is smaller')
    return result

if __name__ == '__main__':
    length_a = 30
    length_b = 20
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")
    
    length_a = 15
    length_b = 25
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")
    
    length_a = 40
    length_b = 40
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")