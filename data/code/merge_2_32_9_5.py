if __name__ == '__main__':
    unsorted_list = [1, 2, 3, 4, 2, 5, 1, 6, 3]
    unique_items_set = set(unsorted_list)
    unique_count = len(unique_items_set)
    print(f"The original list is: {unsorted_list}")
    print(f"The set of unique items is: {unique_items_set}")
    print(f"The number of unique items is: {unique_count}")