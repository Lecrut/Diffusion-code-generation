def sum_even_values(d):
    return sum(value for key, value in d.items() if isinstance(key, int) and isinstance(value, int) and value % 2 == 0)

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 'a': 5, 6: 7}
    print(sum_even_values(sample_dict))