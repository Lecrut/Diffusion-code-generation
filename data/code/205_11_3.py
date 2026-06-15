def sort_items(numbers):
    return sorted(numbers, reverse=True)
if __name__ == '__main__':
    unsorted_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sort_items(unsorted_list)
    print(sorted_list)