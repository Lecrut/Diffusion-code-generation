def find_longest_string(strings: list[str]) -> str:
    if not strings:
        return ""
    
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date", "elderberry"]
    longest_str = find_longest_string(sample_data)
    print(longest_str)