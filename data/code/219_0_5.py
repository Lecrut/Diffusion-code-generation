def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    data1 = [1, 5, 2, 8, 3]
    data2 = [-10, -5, -20, -1]
    data3 = [42]
    data4 = []
    print(f"Max of {data1}: {find_max(data1)}")
    print(f"Max of {data2}: {find_max(data2)}")
    print(f"Max of {data3}: {find_max(data3)}")
    try:
        find_max(data4)
    except ValueError as e:
        print(f"Error for {data4}: {e}")