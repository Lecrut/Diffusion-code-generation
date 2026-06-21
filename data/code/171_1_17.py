def store_name_lengths(store_names):
    return {name.lower(): len(name) for name in store_names}

if __name__ == '__main__':
    sample_names = ['Apple', 'Banana', 'apple', 'Cherry']
    print(store_name_lengths(sample_names))