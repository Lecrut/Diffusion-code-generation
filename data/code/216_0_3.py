import math
def find_middle_value(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_index_right = n // 2
        middle_index_left = middle_index_right - 1
        middle_value = (data[middle_index_left] + data[middle_index_right]) / 2.0
        return middle_value
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5.5, 6.5, 7.5]
    list4 = [1, 2, 3, 4]
    list5 = []
    print(f"Middle value of {list1}: {find_middle_value(list1)}")
    print(f"Middle value of {list2}: {find_middle_value(list2)}")
    print(f"Middle value of {list3}: {find_middle_value(list3)}")
    print(f"Middle value of {list4}: {find_middle_value(list4)}")
    try:
        find_middle_value(list5)
    except ValueError as e:
        print(f"Error for list5: {e}")