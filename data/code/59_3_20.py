MIDDLE_INDEX = lambda length: length // 2

def find_middle_element(lst):
    if len(lst) % 2 == 0:
        raise ValueError("List must have an odd length.")
    return lst[MIDDLE_INDEX(len(lst))]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(find_middle_element(sample_list))