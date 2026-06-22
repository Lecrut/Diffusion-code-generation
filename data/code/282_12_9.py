def calculate_total(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9]
    total = calculate_total(sample_values)
    print(total)