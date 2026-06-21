MAX_VALUE = float('-inf')

def find_max(numbers):
    current_max = MAX_VALUE
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max

if __name__ == '__main__':
    sample_data = [10, 5, 22, 8, 30, 15]
    largest_number = find_max(sample_data)
    print(largest_number)