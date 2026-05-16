def safe_get_second(data):
    if len(data) >= 2:
        return data[1]
    return None
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5]
    list3 = []
    list4 = [1]
    print(f"List 1: {safe_get_second(list1)}")
    print(f"List 2: {safe_get_second(list2)}")
    print(f"List 3: {safe_get_second(list3)}")
    print(f"List 4: {safe_get_second(list4)}")