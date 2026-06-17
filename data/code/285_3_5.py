def check_descending(strings):
    n = len(strings)
    for i in range(n - 1):
        if strings[i] < strings[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry"]
    print(f"List 1: {check_descending(list1)}")
    list2 = ["zebra", "yak", "ant"]
    print(f"List 2: {check_descending(list2)}")
    list3 = ["a", "b", "c"]
    print(f"List 3: {check_descending(list3)}")
    list4 = ["c", "b", "a"]
    print(f"List 4: {check_descending(list4)}")
    list5 = ["hello", "world", "test"]
    print(f"List 5: {check_descending(list5)}")
    list6 = ["apple", "apricot", "banana"]
    print(f"List 6: {check_descending(list6)}")