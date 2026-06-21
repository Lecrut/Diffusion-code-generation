LIST1 = [1, 2, 3]
LIST2 = [4, 5, 6]

def merge_lists(list_a, list_b):
    return list_a + list_b
if __name__ == '__main__':
    combined = merge_lists(LIST1, LIST2)
    print(combined)