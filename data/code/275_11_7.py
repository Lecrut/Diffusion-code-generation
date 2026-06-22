def sum_even_values(data):
    total = 0
    for key, value in data.items():
        if isinstance(value, int) and value % 2 == 0:
            total += value
    return total

if __name__ == '__main__':
    sample_data = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    print(sum_even_values(sample_data))