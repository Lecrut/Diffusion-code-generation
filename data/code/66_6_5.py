import sys
def is_sorted(data):
    n = len(data)
    if n <= 1:
        return True
    for i in range(n - 1):
        if data[i] > data[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 3, 2, 4, 5]
    list3 = [5, 4, 3, 2, 1]
    list4 = [10]
    list5 = []
    print(f"List 1 sorted: {is_sorted(list1)}")
    print(f"List 2 sorted: {is_sorted(list2)}")
    print(f"List 3 sorted: {is_sorted(list3)}")
    print(f"List 4 sorted: {is_sorted(list4)}")
    print(f"List 5 sorted: {is_sorted(list5)}")