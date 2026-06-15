import sys
def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30]
    result = find_maximum(input_data)
    print(result)