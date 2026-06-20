def sum_three_numbers(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sample_values = {1: 3, 2: 5, 3: 7}
    result = sum_three_numbers(sample_values[1], sample_values[2], sample_values[3])
    print(result)