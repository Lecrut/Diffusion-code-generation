def mm_to_inches(mm):
    if not isinstance(mm, (int, float)) or mm < 0:
        raise ValueError("Invalid input: must be a non-negative number")
    return mm * 0.0393701

if __name__ == '__main__':
    sample_mm_values = [25, 100, -10]
    for mm in sample_mm_values:
        try:
            inches = mm_to_inches(mm)
            print(f"{mm} mm is equal to {inches:.4f} inches")
        except ValueError as e:
            print(e)