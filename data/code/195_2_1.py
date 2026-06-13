import sys
def strictly_equal(list1, list2):
    return list1 == list2
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 3, 5]
    list_d = [4, 3, 2, 1]
    print(f"list_a == list_b: {strictly_equal(list_a, list_b)}")
    print(f"list_a == list_c: {strictly_equal(list_a, list_c)}")
    print(f"list_b == list_d: {strictly_equal(list_b, list_d)}")