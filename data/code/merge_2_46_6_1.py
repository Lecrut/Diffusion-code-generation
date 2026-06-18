import sys
def generate_differences(values):
    current = next(iter(values)) if values else 0
    for val in values:
        yield val - current
        current = val
if __name__ == '__main__':
    sample_data = [1, 5, 3, 8, 2]
    diff_gen = generate_differences(sample_data)
    print("Differences:", list(diff_gen))