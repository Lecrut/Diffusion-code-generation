def compare_lists(list1, list2):
    for index in range(min(len(list1), len(list2))):
        if list1[index] > list2[index]:
            print(f"Element at index {index}: {list1[index]} > {list2[index]}")

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [10, 25, 30, 50]
    compare_lists(list_a, list_b)