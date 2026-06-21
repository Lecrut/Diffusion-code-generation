def find_longest_string(iterable: list[str]) -> str:
    if not iterable:
        raise ValueError("The input list is empty")
    longest_string = max(iterable, key=len)
    return longest_string

if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    try:
        longest = find_longest_string(data)
        print(longest)
    except ValueError as e:
        print(e)