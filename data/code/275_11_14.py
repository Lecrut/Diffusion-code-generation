def sum_even_values(d):
    return sum(value for key, value in d.items() if isinstance(value, int) and value % 2 == 0)

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    print(sum_even_values(sample_dict))