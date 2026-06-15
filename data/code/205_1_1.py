def sort_small_list(data):
    new_list = sorted(data, reverse=True)
    return new_list
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    sorted_list = sort_small_list(sample_list)
    print(sorted_list)