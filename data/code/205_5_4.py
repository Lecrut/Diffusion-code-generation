import random
def sort_list(data):
    data.sort()
    return data
if __name__ == '__main__':
    unsorted_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sort_list(unsorted_list)
    print(sorted_list)