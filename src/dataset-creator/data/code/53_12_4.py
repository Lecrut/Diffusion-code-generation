def count_items_from_start(data):
    return len([x for x in data if True])
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b'] * 1000000
    result = count_items_from_start(sample_data)
    print(result)