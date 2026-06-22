def print_strings_with_exclamation(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    for string in strings:
        print(f"{string}!")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    print_strings_with_exclamation(sample_values)