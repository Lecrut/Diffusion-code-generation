INPUT_DATA = [10, 5, 20, 15, 30]

def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    result = find_largest_number(INPUT_DATA)
    print(result)