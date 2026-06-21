def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    return max(data)

if __name__ == '__main__':
    list1 = [10, 5, 20, 8]
    print(f"Largest in {list1}: {find_largest(list1)}")
    list2 = [-5, -1, -10, -2]
    print(f"Largest in {list2}: {find_largest(list2)}")
    list3 = [3.14, 2.71, 1.618]
    print(f"Largest in {list3}: {find_largest(list3)}")
    list4 = [42]
    print(f"Largest in {list4}: {find_largest(list4)}")