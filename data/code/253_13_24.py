def find_the_middle_value_among_three_rank_samples(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_values = {
        'sample1': (3, 1, 2),
        'sample2': (5, -1, 0),
        'sample3': (7, 7, 7)
    }
    
    for key, values in sample_values.items():
        middle_value = find_the_middle_value_among_three_rank_samples(*values)
        print(f"{key}: {middle_value}")