def find_longest_string(strings: list) -> str:
    if not strings:
        return ""
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))