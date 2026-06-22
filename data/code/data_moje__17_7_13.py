def get_last_entry(collection):
    if not collection:
        return None
    return collection[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_entry(sample_list))