INTERSECT_THRESHOLD = 1000

def intersect_lists(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2][:INTERSECT_THRESHOLD]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5, 6] * 100
    sample_list2 = [4, 5, 5, 7, 8] * 200
    print(intersect_lists(sample_list1, sample_list2))