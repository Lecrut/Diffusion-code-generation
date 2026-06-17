def count_items(data):
    return len([i for i in range(len(data))]) if isinstance(data, (list, tuple)) else 0
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    print(count_items(sample_list))
    print(count_items(sample_tuple))