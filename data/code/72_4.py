def compare_lists(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] > list2[i]:
            print(f"List1[{i}] ({list1[i]}) is strictly greater than List2[{i}] ({list2[i]})")
if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [5, 15, 25, 35, 60]
    compare_lists(list_a, list_b)