def get_last_entry(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_entry(sample_list)
    print(result)