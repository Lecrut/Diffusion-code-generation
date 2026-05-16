import math
def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        middle_value = (data[middle_index_1] + data[middle_index_2]) // 2
        return middle_value
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = find_middle_element(sample_list)
    print(result)