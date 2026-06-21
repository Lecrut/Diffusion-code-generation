def find_longest_string(strings: list[str]) -> str:
    if not strings:
        return ""
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    print(find_longest_string(data))