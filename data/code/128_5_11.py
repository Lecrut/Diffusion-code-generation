def check_negatives(numbers):
    for number in numbers:
        if number < 0:
            return True
    return False

if __name__ == '__main__':
    sample_values = [1, -2, 3, 4, 5]
    print(check_negatives(sample_values))