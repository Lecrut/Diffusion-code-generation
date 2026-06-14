import sys
def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    data1 = [1234567890123456789, 9876543210987654321, 5555555555555555555]
    data2 = [-100, -50, -1, -200]
    data3 = [10000000000000000000, 9999999999999999999, 10000000000000000000]
    data4 = []
    print(f"Largest in data1: {find_largest(data1)}")
    print(f"Largest in data2: {find_largest(data2)}")
    print(f"Largest in data3: {find_largest(data3)}")
    try:
        find_largest(data4)
    except ValueError as e:
        print(f"Error for data4: {e}")