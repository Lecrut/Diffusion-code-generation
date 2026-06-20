from collections import Counter

def find_repeated_characters(s):
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    test_string = "programming"
    result = find_repeated_characters(test_string)
    print(result)