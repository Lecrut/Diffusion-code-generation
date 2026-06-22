def create_row(start_val, end_val, multiplier_base):
    if start_val < 1 or end_val > 100 or start_val > end_val:
        raise ValueError("Range must be within 1 to 100 and start <= end")
    return [multiplier_base * col for col in range(start_val, end_val + 1)]

def generate_multiplication_grid(min_val=1, max_val=10):
    try:
        if min_val < 1 or max_val < min_val or max_val > 100:
            raise ValueError("Invalid range for multiplication grid")
        return [create_row(min_val, max_val, row) for row in range(min_val, max_val + 1)]
    except ValueError as e:
        raise ValueError(f"Grid generation failed: {e}")

if __name__ == '__main__':
    sample_min = 1
    sample_max = 10
    result_grid = generate_multiplication_grid(sample_min, sample_max)
    for row_index, row_values in enumerate(result_grid):
        print(f"Row {sample_min + row_index}: {row_values}")