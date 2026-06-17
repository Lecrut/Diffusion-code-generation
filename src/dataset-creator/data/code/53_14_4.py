def count_items(data):
    return sum(1 for _ in data) if isinstance(data, (list, tuple)) else 0
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b')
    print(count_items(sample_list))
    print(count_items(sample_tuple))