def print_strings_with_exclamation(strings):
    for string in strings:
        result = f"{string}!"
        print(result)

if __name__ == '__main__':
    sample_values = ("Python", "is", "awesome!")
    print_strings_with_exclamation(sample_values)