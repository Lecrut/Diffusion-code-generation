MIDDLE_INDEX = lambda n: (n - 1) // 2

def find_middle_element(lst):
    return lst[MIDDLE_INDEX(len(lst))]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1, 4]
    print(find_middle_element(sample_list))