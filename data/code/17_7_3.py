def get_last_entry(collection):
    if not collection:
        raise ValueError("Collection cannot be empty")
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_entry(sample_list)
    print(result)