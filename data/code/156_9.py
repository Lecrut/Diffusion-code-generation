def find_list_average(data):
    if not isinstance(data, list):
        return None
    if not data:
        return 0
    try:
        total = sum(data)
        average = total / len(data)
        return average
    except TypeError:
        return None
    except Exception:
        return None
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = ["a", "b", "c"]
    list4 = [10, 20, "error"]
    list5 = None
    list6 = [5.5, 10.5]
    print(f"Average of {list1}: {find_list_average(list1)}")
    print(f"Average of {list2}: {find_list_average(list2)}")
    print(f"Average of {list3}: {find_list_average(list3)}")
    print(f"Average of {list4}: {find_list_average(list4)}")
    print(f"Average of {list5}: {find_list_average(list5)}")
    print(f"Average of {list6}: {find_list_average(list6)}")