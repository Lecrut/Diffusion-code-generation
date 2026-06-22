MIN_VALUE = "a"

def find_min_lexicographical(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    min_str = MIN_VALUE
    for string in strings:
        if string < min_str:
            min_str = string
    return min_str

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_min_lexicographical(sample_strings))