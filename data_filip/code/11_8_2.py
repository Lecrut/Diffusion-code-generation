def find_chars_appearing_twice(s):
    from collections import Counter
    counts = Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_string = "abracadabra"
    print(find_chars_appearing_twice(sample_string))
    sample_string2 = "hello world"
    print(find_chars_appearing_twice(sample_string2))
    sample_string3 = "aabbccddeeff"
    print(find_chars_appearing_twice(sample_string3))