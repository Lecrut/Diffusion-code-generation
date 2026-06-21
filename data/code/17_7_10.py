def get_last_entry(collection):
    if not collection:
        return None
    return collection[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_entry(sample_data)
    print(result)