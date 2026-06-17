import sys
def generate_differences(values):
    prev = next(iter(values)) if not isinstance(values, list) else None
    for val in values:
        yield (val - prev) if prev is not None else 0
        prev = val
if __name__ == '__main__':
    sample_data = [10, 25, 37, 48, 60]
    diff_gen = generate_differences(sample_data)
    print("Differences:")
    for i, d in enumerate(diff_gen):
        if i > 0:
            print(f"Value {sample_data[i]} - Value {sample_data[i-1]} = {d}")