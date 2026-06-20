def compare_elements(data):
    if len(data) < 6:
        return False
    return data[0] > data[5]

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [5, 15, 25, 35, 45]
    print(f"Comparing {list1[0]} and {list2[5]}: {compare_elements(list1)}")
    print(f"Comparing {list1[1]} and {list2[5]}: {compare_elements(list2)}")