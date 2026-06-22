def find_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    LIST_MINIMUM_SIZE = 1
    index = (len(lst) - 1) // 2
    return lst[index]

if __name__ == '__main__':
    odd_case = [99, 88, 77, 66, 55]
    even_case = [1, 2, 3, 4]
    print(find_middle_element(odd_case))
    print(find_middle_element(even_case))