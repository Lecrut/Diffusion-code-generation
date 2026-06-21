def sum_list_elements(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    result = sum_list_elements(sample_values)
    print(result)