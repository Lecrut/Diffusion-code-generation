if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    unique_items = set(sample_list)
    item_counts = [(item, sample_list.count(item)) for item in unique_items]
    print(item_counts)