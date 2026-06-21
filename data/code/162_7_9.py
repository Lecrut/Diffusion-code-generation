def name_lengths(names):
    return {name: len(name) for name in names}

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'David']
    print(name_lengths(sample_names))