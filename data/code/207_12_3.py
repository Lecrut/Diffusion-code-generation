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
    sample_numbers = [15, 3, 88, 42, 9]
    result = find_largest(sample_numbers)
    if result is not None:
        print(result)
    else:
        print("The list is empty")