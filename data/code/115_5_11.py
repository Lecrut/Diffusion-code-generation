def divide_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    return [num1 / num2 for num1, num2 in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 15, 7]
    sample_list2 = [2, 3, 0]
    try:
        result = divide_lists(sample_list1, sample_list2)
        print(f"Result of division: {result}")
    except ValueError as err:
        print(f"Error caught: {err}")