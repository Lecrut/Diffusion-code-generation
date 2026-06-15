def sort_items(data):
    return sorted(data, reverse=True)
if __name__ == '__main__':
    unsorted_numbers = [5, 1, 9, 3, 7]
    sorted_numbers = sort_items(unsorted_numbers)
    print(sorted_numbers)