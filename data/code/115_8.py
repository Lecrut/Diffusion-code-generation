def elementwise_divide(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have equal length")
    result = []
    for i in range(len(list1)):
        result.append(list1[i] / list2[i])
    return result
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [2, 4, 5, 10]
    try:
        division_result = elementwise_divide(list_a, list_b)
        print(division_result)
    except ValueError as e:
        print(f"Error: {e}")