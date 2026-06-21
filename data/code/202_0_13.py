MAX_VALUE = float('-inf')

def find_maximum(numbers):
    global MAX_VALUE
    for number in numbers:
        if number > MAX_VALUE:
            MAX_VALUE = number
    return MAX_VALUE

if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30, 15]
    largest_number = find_maximum(input_data)
    print(largest_number)