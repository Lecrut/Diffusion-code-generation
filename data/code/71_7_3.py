import math
def find_middle_arithmetic(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        middle_index = n // 2
        middle_element = data[middle_index]
    else:
        middle_index = (n - 1) // 2
        middle_element = data[middle_index]
    return middle_element
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result1 = find_middle_arithmetic(sample_list)
    print(result1)
    sample_list_even = [1, 2, 3, 4, 5, 6]
    result2 = find_middle_arithmetic(sample_list_even)
    print(result2)
    sample_list_single = [99]
    result3 = find_middle_arithmetic(sample_list_single)
    print(result3)
    sample_list_empty = []
    result4 = find_middle_arithmetic(sample_list_empty)
    print(result4)