def get_last_entry(data_collection):
    if not data_collection:
        return None
    return data_collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_entry(sample_list)
    print(result)