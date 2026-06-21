LIST1 = [1, 2, 3]
LIST2 = [4, 5, 6]

def combine_lists(list_a=LIST1, list_b=LIST2):
    return list_a + list_b
if __name__ == '__main__':
    result = combine_lists()
    print(result)