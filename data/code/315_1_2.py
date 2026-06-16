def generate_repeating_pattern(start, end, cycle_length):
    if cycle_length <= 0:
        return []
    pattern = []
    for i in range(start, end + 1):
        index = i - start
        pattern.append(str(start + (index % cycle_length)))
    return pattern
if __name__ == '__main__':
    start_val = 1
    end_val = 20
    cycle_len = 3
    result = generate_repeating_pattern(start_val, end_val, cycle_len)
    print(result)