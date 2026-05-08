def sort_list(data):
    data.sort()
    return data
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    print("Original list:", sample_list)
    sorted_list = sort_list(sample_list)
    print("Sorted list:", sorted_list)