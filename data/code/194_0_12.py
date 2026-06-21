def find_longest_string(strings):
    if not strings:
        return None
    MAX_LENGTH = len(max(strings, key=len))
    longest_string = max(filter(lambda s: len(s) == MAX_LENGTH, strings), default=None)
    return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)