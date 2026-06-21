MAX_LENGTH = float('-inf')

def find_longest_string(strings: list[str]) -> str:
    longest_string = ""
    for s in strings:
        if len(s) > MAX_LENGTH:
            MAX_LENGTH = len(s)
            longest_string = s
    return longest_string

if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    longest = find_longest_string(sample_data)
    print(longest)