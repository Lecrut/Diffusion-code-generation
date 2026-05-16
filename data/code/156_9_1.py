def find_list_average(data):
    if not isinstance(data, list):
        return None
    if not data:
        return 0
    try:
        return sum(data) / len(data)
    except TypeError:
        return None
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [10.5, 20.5, 30.5]
    list4 = "not a list"
    list5 = [1, 2, "three"]
    list6 = []
    print(f"Average of {list1}: {find_list_average(list1)}")
    print(f"Average of {list2}: {find_list_average(list2)}")
    print(f"Average of {list3}: {find_list_average(list3)}")
    print(f"Average of {list4}: {find_list_average(list4)}")
    print(f"Average of {list5}: {find_list_average(list5)}")
    print(f"Average of {list6}: {find_list_average(list6)}")