def print_separated_with_index(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    
    for index, string in enumerate(strings, start=1):
        print(f"{index}. {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    try:
        print_separated_with_index(sample_strings)
    except ValueError as e:
        print(e)