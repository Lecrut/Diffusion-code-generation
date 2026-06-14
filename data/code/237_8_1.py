def generate_sequence(start_value, growth_factor):
    current_value = start_value
    for _ in range(10):
        print(current_value)
        current_value *= growth_factor
if __name__ == '__main__':
    start = 2
    factor = 1.5
    generate_sequence(start, factor)