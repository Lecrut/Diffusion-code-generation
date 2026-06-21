if __name__ == '__main__':
    sample_list = ['red', 'blue', 'green', 'blue', 'red', 'red']
    unique_items = set(sample_list)
    item_counts = [(item, sample_list.count(item)) for item in unique_items]
    print(item_counts)