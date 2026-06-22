EXCLAMATION_MARK = '!'

def print_strings_with_exclamation(strings):
    for s in strings:
        print(f"{s}{EXCLAMATION_MARK}")

if __name__ == '__main__':
    sample_values = ("Hello", "World", "Python")
    print_strings_with_exclamation(sample_values)