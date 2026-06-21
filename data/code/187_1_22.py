MAX_NUMBER = float('-inf')

def find_max(numbers):
    largest = MAX_NUMBER
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    print(find_max(sample_values))