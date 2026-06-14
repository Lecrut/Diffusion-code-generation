def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, 5.2, -3.14, 9.9]
    data3 = [42.0]
    data4 = []
    print(f"Minimum of {data1}: {find_minimum(data1)}")
    print(f"Minimum of {data2}: {find_minimum(data2)}")
    print(f"Minimum of {data3}: {find_minimum(data3)}")
    try:
        find_minimum(data4)
    except ValueError as e:
        print(f"Error for {data4}: {e}")