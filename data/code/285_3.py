def check_descending(strings):
    n = len(strings)
    for i in range(n - 1):
        if strings[i] < strings[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry"]
    print(check_descending(list1))
    list2 = ["zebra", "yak", "ant"]
    print(check_descending(list2))
    list3 = ["a", "b", "c", "d"]
    print(check_descending(list3))
    list4 = ["c", "b", "a"]
    print(check_descending(list4))
    list5 = ["hello", "world", "test"]
    print(check_descending(list5))