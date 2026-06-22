MAX_VALUE_DEFAULT = float('-inf')

def find_maximum(numbers):
    if not numbers:
        return MAX_VALUE_DEFAULT
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
if __name__ == '__main__':
    sample_numbers = [3, 5, -2, 8, 1]
    print(find_maximum(sample_numbers))