def compare_lengths(len1, len2):
    return 'len1 is greater' if len1 > len2 else ('len2 is smaller' if len1 < len2 else 'equal')

if __name__ == '__main__':
    a = 15
    b = 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    
    a = 7
    b = 20
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    
    a = 10
    b = 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    
    a = 30
    b = 25
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")