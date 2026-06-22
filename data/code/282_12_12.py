def calculate_total(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.3, 3.7, 4.1]
    result = calculate_total(sample_numbers)
    print(result)