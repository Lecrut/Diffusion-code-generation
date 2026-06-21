def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577, 9.81]
    data2 = [-10.5, 5.2, -3.1, 0.0, 1.1]
    data3 = [42.0]
    data4 = [7.777, 7.778, 7.7770]
    print(f"Smallest in {data1}: {find_smallest(data1)}")
    print(f"Smallest in {data2}: {find_smallest(data2)}")
    print(f"Smallest in {data3}: {find_smallest(data3)}")
    print(f"Smallest in {data4}: {find_smallest(data4)}")