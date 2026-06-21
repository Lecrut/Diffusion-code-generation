def find_largest(a, b, c):
    candidates = [a, b, c]
    return max(candidates)

if __name__ == '__main__':
    sample_values = {
        'set_one': [150, 300, 225],
        'set_two': [10, 99, 5],
        'set_three': [-5, -1, -100]
    }
    for key, values in sample_values.items():
        a, b, c = values[0], values[1], values[2]
        max_val = find_largest(a, b, c)
        print(f"{key}: {max_val}")