def count_unique_items(data_list):
    unique_set = set(data_list)
    return len(unique_set)
if __name__ == '__main__':
    unsorted_list = [1, 2, 3, 4, 2, 5, 1, 6, 3]
    unique_count = count_unique_items(unsorted_list)
    print(f"The original list is: {unsorted_list}")
    print(f"The number of unique items is: {unique_count}")