def sum_even_values(input_dict):
    total = 0
    for value in input_dict.values():
        if isinstance(value, int) and value % 2 == 0:
            total += value
    return total

if __name__ == '__main__':
    sample_dict = {1: 34, 2: 'hello', 3: 56, 4: 78.9, 5: 100}
    result = sum_even_values(sample_dict)
    print(result)