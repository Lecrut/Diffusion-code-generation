def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, -5.2, -20.1, -1.9]
    data3 = [42.0]
    data4 = []
    print(f"Maximum of {data1}: {find_maximum(data1)}")
    print(f"Maximum of {data2}: {find_maximum(data2)}")
    print(f"Maximum of {data3}: {find_maximum(data3)}")
    try:
        find_maximum(data4)
    except ValueError as e:
        print(f"Error for {data4}: {e}")