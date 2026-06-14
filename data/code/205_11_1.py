def sort_items(data):
    return sorted(data, reverse=True)
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sort_items(sample_list)
    print(sorted_list)