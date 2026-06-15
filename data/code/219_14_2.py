import sys
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    input_data = [15, 8, 42, 3, 99, 21]
    result = find_largest(input_data)
    print(result)