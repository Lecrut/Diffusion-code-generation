def get_last_entry(collection):
    if not collection:
        return None
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 60]
    result = get_last_entry(sample_list)
    print(result)