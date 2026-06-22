def print_reversed_strings(strings):
    if not all(isinstance(item, str) for item in strings):
        raise ValueError("All items must be strings")
    
    reversed_strings = [item[::-1] for item in strings]
    return reversed_strings

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    try:
        reversed_values = print_reversed_strings(sample_values)
        print(reversed_values)
    except ValueError as e:
        print(e)