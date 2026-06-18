def check_positive(result):
    if result > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.5]
    for val in sample_values:
        is_pos = check_positive(val)
        print(f"Result {val} -> Positive: {is_pos}")