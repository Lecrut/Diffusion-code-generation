MAX_LIST_LENGTH = 10

def max_pairs(list1, list2):
    return [max(a, b) for a, b in zip(list1[:MAX_LIST_LENGTH], list2[:MAX_LIST_LENGTH])]

if __name__ == '__main__':
    sample_list1 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    sample_list2 = [3, 9, 7, 15, 11, 13, 17, 19, 21, 23]
    result = max_pairs(sample_list1, sample_list2)
    print(result)