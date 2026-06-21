MAX_LEN = 1024

def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input is not iterable")
    longest_str = ""
    for item in lst:
        if isinstance(item, str) and len(item) > len(longest_str):
            longest_str = item
    return longest_str if len(longest_str) <= MAX_LEN else longest_str[:MAX_LEN]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", 123, None]
    try:
        result = longest_string(sample_list)
        print(result)
    except ValueError as e:
        print(e)