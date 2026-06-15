def reverse_list(data):
    return data[::-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [7]
    list4 = ['a', 'b', 'c']
    list5 = [99]
    print(f"Reversing {list1}: {reverse_list(list1)}")
    print(f"Reversing {list2}: {reverse_list(list2)}")
    print(f"Reversing {list3}: {reverse_list(list3)}")
    print(f"Reversing {list4}: {reverse_list(list4)}")
    print(f"Reversing {list5}: {reverse_list(list5)}")