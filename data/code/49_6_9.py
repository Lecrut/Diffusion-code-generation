def compare_lengths(len1, len2):
    result = "len1 is greater" if len1 > len2 else "len2 is greater"
    return result if len1 != len2 else "equal"

if __name__ == '__main__':
    length_a = 50
    length_b = 30
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")
    
    length_a = 20
    length_b = 40
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")
    
    length_a = 75
    length_b = 75
    print(f"Comparing {length_a} and {length_b}: {compare_lengths(length_a, length_b)}")