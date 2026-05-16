import collections
def find_duplicates(s):
    char_counts = collections.defaultdict(int)
    duplicates = set()
    for char in s:
        char_counts[char] += 1
        if char_counts[char] > 1:
            duplicates.add(char)
    return list(duplicates)
if __name__ == '__main__':
    test_string1 = "programming"
    result1 = find_duplicates(test_string1)
    print(f"Input: {test_string1}")
    print(f"Duplicates: {result1}")
    test_string2 = "hello world"
    result2 = find_duplicates(test_string2)
    print(f"Input: {test_string2}")
    print(f"Duplicates: {result2}")
    test_string3 = "abcde"
    result3 = find_duplicates(test_string3)
    print(f"Input: {test_string3}")
    print(f"Duplicates: {result3}")
    test_string4 = "aabbccddeeff"
    result4 = find_duplicates(test_string4)
    print(f"Input: {test_string4}")
    print(f"Duplicates: {result4}")