def compare_lists(list1, list2):
    for i, (a, b) in enumerate(zip(list1, list2)):
        if a > b:
            print(f"Element at index {i} in list1 is greater than the element at the same index in list2.")

if __name__ == '__main__':
    compare_lists([5, 3, 9, 8], [4, 6, 7, 10])