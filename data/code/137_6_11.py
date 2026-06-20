def check_range(value):
    return 1 <= value <= 10

if __name__ == '__main__':
    sample_values = [5, 0, 10, 11, -1]
    for val in sample_values:
        print(f"Value {val} within range: {check_range(val)}")