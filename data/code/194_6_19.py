def find_longest_string(string_iterable: list) -> str:
    if not string_iterable:
        return ""
    
    longest_string = max(string_iterable, key=len)
    return longest_string

if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    print(find_longest_string(data))