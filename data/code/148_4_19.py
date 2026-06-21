MAX_VALUE = float('-inf')

def find_largest(numbers):
    largest = MAX_VALUE
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, -5.2, -20.1, -1.0]
    data3 = [1.0, 1.0, 1.0, 1.0]
    data4 = [99.99999999999999, 100.0]
    print(f"Largest in {data1}: {find_largest(data1)}")
    print(f"Largest in {data2}: {find_largest(data2)}")
    print(f"Largest in {data3}: {find_largest(data3)}")
    print(f"Largest in {data4}: {find_largest(data4)}")