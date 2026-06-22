def validate_mm(mm):
    if not isinstance(mm, (int, float)) or mm < 0:
        raise ValueError("mm must be a non-negative number")

def mm_to_inches(mm):
    validate_mm(mm)
    return mm * 0.0393701

if __name__ == '__main__':
    sample_values = [25, 100, 500]
    for value in sample_values:
        print(f"{value} mm is equal to {mm_to_inches(value):.4f} inches")