def print_strings_separately(strings):
    string_dict = {
        'type': 'strings',
        'items': strings
    }
    for item in string_dict['items']:
        print(item)

if __name__ == '__main__':
    sample_tuple = ('Hello', 'World')
    print_strings_separately(sample_tuple)