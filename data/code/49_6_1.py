def compare_lengths(len1, len2):
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'
if __name__ == '__main__':
    a = 10
    b = 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    a = 25
    b = 15
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    a = 5
    b = 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    a = 100
    b = 99
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")