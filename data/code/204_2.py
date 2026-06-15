def find_middle_element(data: list[float]) -> float:
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    if n % 2 == 1:
        return data[n // 2]
    else:
        middle_right = n // 2
        middle_left = middle_right - 1
        return (data[middle_left] + data[middle_right]) / 2.0
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [7.0, 8.0, 9.0]
    list4 = [100]
    list5 = []
    print(f"Middle element of {list1}: {find_middle_element(list1)}")
    print(f"Middle element of {list2}: {find_middle_element(list2)}")
    print(f"Middle element of {list3}: {find_middle_element(list3)}")
    print(f"Middle element of {list4}: {find_middle_element(list4)}")
    try:
        find_middle_element(list5)
    except ValueError as e:
        print(f"Error for {list5}: {e}")