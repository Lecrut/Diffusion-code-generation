def list_sum(iterable):
    return sum(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, -5, 20, 0]
    list3 = []
    list4 = [3.5, 1.5, 5.0]
    print(f"Sum of {list1}: {list_sum(list1)}")
    print(f"Sum of {list2}: {list_sum(list2)}")
    print(f"Sum of {list3}: {list_sum(list3)}")
    print(f"Sum of {list4}: {list_sum(list4)}")