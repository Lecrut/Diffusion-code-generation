def compute_sum(eight_numbers):
    total = 0
    for num in eight_numbers:
        total += num
    return total

if __name__ == '__main__':
    sample_values = (12, 24, 36, 48, 60, 72, 84, 96)
    result = compute_sum(sample_values)
    print(result)