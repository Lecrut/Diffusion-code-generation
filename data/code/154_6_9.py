if __name__ == '__main__':
    sample_list = [42, 'hello', 42, 3.14, 'world', 'hello']
    item_counts = [(item, sample_list.count(item)) for item in set(sample_list)]
    print(item_counts)