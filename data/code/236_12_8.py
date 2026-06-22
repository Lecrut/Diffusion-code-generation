SAMPLE_LIST = [1, 2, 3]
NUM_COPIES = 3

def extend_list_with_last_element(lst, n):
    lst.extend([lst[-1]] * n)

if __name__ == '__main__':
    result = SAMPLE_LIST[:]
    extend_list_with_last_element(result, NUM_COPIES)
    print(result)