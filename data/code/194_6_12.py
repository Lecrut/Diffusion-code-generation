def find_longest_string(string_list: list[str]) -> str:
    if not string_list:
        return ""
    longest = max(string_list, key=len)
    return longest

if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    longest_string = find_longest_string(sample_data)
    print(longest_string)