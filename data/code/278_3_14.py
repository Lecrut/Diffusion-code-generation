EXCLAMATION = "!"

def print_strings_with_exclamation(strings):
    for s in strings:
        print(f"{s}{EXCLAMATION}")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    print_strings_with_exclamation(sample_values)