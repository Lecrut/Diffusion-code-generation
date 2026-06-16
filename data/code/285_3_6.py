def check_descending(strings):
    n = len(strings)
    for i in range(n - 1):
        if strings[i] < strings[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry"]
    list2 = ["zebra", "yak", "ant"]
    list3 = ["a", "b", "c", "d"]
    list4 = ["dog", "cat", "bird"]
    print(f"List 1 check: {check_descending(list1)}")
    print(f"List 2 check: {check_descending(list2)}")
    print(f"List 3 check: {check_descending(list3)}")
    print(f"List 4 check: {check_descending(list4)}")