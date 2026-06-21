def store_name_lengths(store_names):
    return {name.lower(): len(name) for name in set(store_names)}

if __name__ == '__main__':
    sample_stores = ['Apple', 'banana', 'Cherry', 'apple']
    print(store_name_lengths(sample_stores))