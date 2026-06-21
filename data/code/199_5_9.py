def filter_names(names):
    return [name for name in names if all(char.isalpha() for char in name)]

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'D@vid', 'Eve']
    filtered_names = filter_names(sample_names)
    print(filtered_names)