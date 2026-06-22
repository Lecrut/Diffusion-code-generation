def sum_even_values(input_dict):
    total = 0
    for key, value in input_dict.items():
        if isinstance(key, int) and isinstance(value, int) and value % 2 == 0:
            total += value
    return total

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    result = sum_even_values(sample_dict)
    print(result)