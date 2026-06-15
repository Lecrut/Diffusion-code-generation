def combine_lists(list1, list2):
    combined = [x + y for x in list1 for y in list2]
    return combined
list_a = [1, 2, 3]
list_b = [10, 20]
result = combine_lists(list_a, list_b)
if __name__ == '__main__':
    print(result)