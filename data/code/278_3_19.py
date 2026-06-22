def print_strings_with_exclamation(strings):
    for s in strings:
        if not s:
            continue
        print(f"{s}!")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "", "Python")
    print_strings_with_exclamation(sample_values)