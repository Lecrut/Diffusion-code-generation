def compare_elements(list1, list2, index):
    if index < len(list1) and index < len(list2):
        return (list1[index], "greater than", list2[index]) if list1[index] > list2[index] else \
               (list1[index], "less than", list2[index]) if list1[index] < list2[index] else \
               (list1[index], "equal to", list2[index])
    else:
        return ("Index out of bounds")

if __name__ == '__main__':
    result = compare_elements([1, 2, 3], [4, 5, 6], 1)
    print(result)