def print_strings_with_exclamation(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the tuple must be strings")
    
    for string in strings:
        result = f"{string}!"
        print(result)

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    print_strings_with_exclamation(sample_values)