import statistics

def compute_min_max(data: list) -> tuple:
    return min(data), max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 8, 2, 9]
    min_value, max_value = compute_min_max(sample_data)
    print(f"Minimum: {min_value}, Maximum: {max_value}")