SEPARATOR = ' '

def split_names(names):
    return [name for name in names.split(SEPARATOR) if name]

if __name__ == '__main__':
    sample_names = "Alice Bob  Charlie   "
    print(split_names(sample_names))