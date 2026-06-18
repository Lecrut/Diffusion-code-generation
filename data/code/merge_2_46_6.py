import sys
def generate_differences(values):
    current = next(iter(values)) if values else 0
    for val in values:
        yield abs(val - current)
        current = val
if __name__ == '__main__':
    sample_data = [1, 5, 3, 8, 2]
    diff_generator = generate_differences(sample_data)
    total_diff = sum(diff_generator)
    print(f"Total absolute difference: {total_diff}")