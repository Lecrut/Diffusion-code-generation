MIDDLE_INDEX = lambda length: length // 2

def find_middle_element(lst):
    return lst[MIDDLE_INDEX(len(lst))]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(find_middle_element(sample_list))