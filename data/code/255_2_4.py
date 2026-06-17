import sys
def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    input_data = [42, 15, 89, 3, 77]
    result = find_maximum(input_data)
    print(result)