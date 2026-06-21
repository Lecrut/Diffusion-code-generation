def accumulate_floats(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5]
    result = accumulate_floats(sample_numbers)
    print(result)