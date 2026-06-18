import time
def is_positive_result(data):
    total = 0
    for item in data:
        try:
            val = float(item)
            total += val
        except (ValueError, TypeError):
            continue
    return total > 0
if __name__ == '__main__':
    sample_data = [1.5, -2.3, 4.7, "invalid", 89]
    start_time = time.perf_counter()
    result = is_positive_result(sample_data)
    end_time = time.perf_counter()
    print(f"Is positive: {result}")
    print(f"Time taken (seconds): {end_time - start_time:.6f}")