def find_longest_string(strings: list) -> str:
    if not strings:
        return ""
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    longest_string = find_longest_string(sample_data)
    print(longest_string)