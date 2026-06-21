def longest_string(strings: list[str]) -> str:
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print(longest_string(sample_strings))