def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, -5.2, -20.8, -1.1]
    data3 = [100.0, 50.5, 200.0, 150.75]
    data4 = [42.0]
    data5 = []
    print(f"Largest in {data1}: {find_largest(data1)}")
    print(f"Largest in {data2}: {find_largest(data2)}")
    print(f"Largest in {data3}: {find_largest(data3)}")
    print(f"Largest in {data4}: {find_largest(data4)}")
    try:
        find_largest(data5)
    except ValueError as e:
        print(f"Error for {data5}: {e}")