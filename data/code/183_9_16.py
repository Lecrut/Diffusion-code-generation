def split_names(name_string):
    return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    sample_names = 'Alice-Bob-Cindy'
    print(split_names(sample_names))