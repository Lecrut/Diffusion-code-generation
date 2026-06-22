def compare_lengths(len1, len2):
    comparison_result = {
        0: 'equal',
        1: 'len1 is greater',
        -1: 'len2 is smaller'
    }
    return comparison_result.get((len1 > len2) - (len1 < len2))

if __name__ == '__main__':
    a, b = 10, 15
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    a, b = 20, 20
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    a, b = 5, 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")