def sum_even_values(input_dict):
    total = 0
    for value in input_dict.values():
        if isinstance(value, int) and value % 2 == 0:
            total += value
    return total

if __name__ == '__main__':
    sample_dict = {1: 3, 2: 4, 3: 'b', 4: 6, 5: 8.0}
    result = sum_even_values(sample_dict)
    print(result)