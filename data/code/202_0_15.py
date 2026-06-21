def find_max(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30, 15]
    print(find_max(input_data))