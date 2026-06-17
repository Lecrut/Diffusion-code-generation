import math
def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    print(f"List: {list1}, Median: {calculate_median(list1)}")
    list2 = [4, 1, 7, 2, 9, 5]
    print(f"List: {list2}, Median: {calculate_median(list2)}")
    list3 = [10, 20, 30, 40]
    print(f"List: {list3}, Median: {calculate_median(list3)}")
    list4 = [5]
    print(f"List: {list4}, Median: {calculate_median(list4)}")
    list5 = []
    try:
        calculate_median(list5)
    except ValueError as e:
        print(f"Error for empty list: {e}")