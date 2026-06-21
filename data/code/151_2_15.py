LIST1 = [1, 2, 3]
LIST2 = [4, 5, 6]

def combine_lists(list1=LIST1, list2=LIST2):
    return list1 + list2

if __name__ == '__main__':
    result = combine_lists()
    print(result)