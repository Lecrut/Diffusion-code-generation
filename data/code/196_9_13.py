SAMPLE_LIST_1 = [1, 2, 3]
SAMPLE_LIST_2 = [4, 5, 6]

def concatenate_lists(list_x, list_y):
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    print(concatenate_lists(SAMPLE_LIST_1, SAMPLE_LIST_2))