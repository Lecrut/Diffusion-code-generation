if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2, 1]
    unique_items = set(sample_list)
    item_counts = [(item, sample_list.count(item)) for item in unique_items]
    print(item_counts)