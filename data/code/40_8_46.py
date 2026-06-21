def print_first_letters(strings):
    for string in strings:
        if string:
            print(string[0])
if __name__ == '__main__':
    sample_strings = ['blueberry', 'cherry', 'dragonfruit', 'elderberry']
    print_first_letters(sample_strings)