def find_the_middle_value_among_three_rank_samples(a, b, c):
    values = sorted([a, b, c])
    return values[1]

if __name__ == '__main__':
    sample_values = {
        'sample1': (3, 1, 2),
        'sample2': (5, 7, 6),
        'sample3': (-1, -3, -2)
    }
    
    for name, values in sample_values.items():
        middle_value = find_the_middle_value_among_three_rank_samples(*values)
        print(f"Middle value of {name}: {middle_value}")