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
    input_data = [15, 8, 22, 4, 30]
    result = find_maximum(input_data)
    print(result)