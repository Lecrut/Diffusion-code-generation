from collections import Counter

def filter_repeated_chars(s):
    counts = Counter(s)
    result_chars = [char for char in s if counts[char] > 1]
    seen = set()
    result_unique_order = []
    for char in result_chars:
        if char not in seen:
            seen.add(char)
            result_unique_order.append(char)
    return ''.join(result_unique_order)

if __name__ == '__main__':
    sample_string = "programming"
    result = filter_repeated_chars(sample_string)
    print(result)
    
    sample_string2 = "aabbccdd"
    result2 = filter_repeated_chars(sample_string2)
    print(result2)
    
    sample_string3 = "abcdef"
    result3 = filter_repeated_chars(sample_string3)
    print(result3)