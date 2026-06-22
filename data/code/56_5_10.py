def validate_range(start, end):
    if start > end:
        raise ValueError("Start cannot be greater than end")
    if start < 1 or end > 100:
        raise ValueError("Range must be between 1 and 100")

def build_grid(start, end):
    validate_range(start, end)
    return [[row * col for col in range(start, end + 1)] for row in range(start, end + 1)]

if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    grid_result = build_grid(sample_start, sample_end)
    for line in grid_result:
        print(line)