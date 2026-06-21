def strip_names(names):
    return [name.strip() for name in names.split(',')]

if __name__ == '__main__':
    sample_input = "Alice, Bob, Charlie"
    print(strip_names(sample_input))