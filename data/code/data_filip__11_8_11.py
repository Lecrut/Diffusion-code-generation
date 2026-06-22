from collections import Counter

def find_chars_appearing_twice(s):
    counts = Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    return sorted(result)

if __name__ == '__main__':
    sample_string = "aabbccddeeffgghhii"
    print(find_chars_appearing_twice(sample_string))
    sample_string_2 = "hello world"
    print(find_chars_appearing_twice(sample_string_2))
    sample_string_3 = "programming"
    print(find_chars_appearing_twice(sample_string_3))