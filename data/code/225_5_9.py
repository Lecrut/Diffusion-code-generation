import statistics

def compute_min_max(data: list) -> tuple:
    return min(data), max(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_val, max_val = compute_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")