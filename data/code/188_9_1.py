def reverse_list(data):
    return data[::-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [7]
    list4 = ['a', 'b', 'c']
    list5 = [99]
    print(f"Original: {list1}, Reversed: {reverse_list(list1)}")
    print(f"Original: {list2}, Reversed: {reverse_list(list2)}")
    print(f"Original: {list3}, Reversed: {reverse_list(list3)}")
    print(f"Original: {list4}, Reversed: {reverse_list(list4)}")
    print(f"Original: {list5}, Reversed: {reverse_list(list5)}")