def count_items(data):
    return sum(1 for _ in data) if hasattr(data, "__iter__") else 0
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    print(count_items(sample_list))
    print(count_items(sample_tuple))