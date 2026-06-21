def find_longest_string(strings):
    return max(strings, key=len) if strings else None

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)