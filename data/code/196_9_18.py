SAMPLE_SIZE = 10**6

def concatenate_lists(list_x, list_y):
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    sample_list1 = list(range(SAMPLE_SIZE))
    sample_list2 = list(range(SAMPLE_SIZE, 2 * SAMPLE_SIZE))
    result = concatenate_lists(sample_list1, sample_list2)
    print(len(result))