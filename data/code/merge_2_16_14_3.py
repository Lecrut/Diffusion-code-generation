def get_list_size(data):
    return len(data)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 'hello', True]
    size = get_list_size(sample_data)
    print(size)