SAMPLE_VALUES = ("Hello", "World", "Python")

def print_strings_with_exclamation(strings):
    for s in strings:
        print(f"{s}!")

if __name__ == '__main__':
    print_strings_with_exclamation(SAMPLE_VALUES)