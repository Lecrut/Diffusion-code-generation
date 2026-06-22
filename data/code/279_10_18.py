def validate_range(start, end):
    if start < 1 or end > 10:
        raise ValueError("Range must be between 1 and 10 inclusive.")

def cycle_range():
    for i in range(1, 11):
        print(i)

if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    validate_range(sample_start, sample_end)
    cycle_range()