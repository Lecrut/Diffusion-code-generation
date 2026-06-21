def strip_names(names):
    return [name.strip() for name in names.split(',')]

if __name__ == '__main__':
    sample_names = "Alice, Bob, Charlie, Dave"
    print(strip_names(sample_names))