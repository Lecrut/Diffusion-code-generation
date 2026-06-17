import sys
def generate_differences(values):
    current = next(iter(values)) if values else 0
    for val in values:
        yield abs(val - current)
        current = val
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    diff_gen = generate_differences(sample_data)
    total_diff = sum(diff_gen)
    print(f"Total absolute difference: {total_diff}")