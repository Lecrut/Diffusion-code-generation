def split_names(name_string):
    return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    sample_names = "John-Doe-Jane-Smith"
    print(split_names(sample_names))