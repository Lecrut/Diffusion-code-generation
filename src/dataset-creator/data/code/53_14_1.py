def count_items(data):
    return len(data) if isinstance(data, (list, tuple)) else 0
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    print(f"List count: {count_items(sample_list)}")
    print(f"Tuple count: {count_items(sample_tuple)}")