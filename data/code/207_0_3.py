def find_maximum(data):
    return max(data)
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = [1000, 500, 750]
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {list3}: {find_maximum(list3)}")
    print(f"Maximum of {list4}: {find_maximum(list4)}")