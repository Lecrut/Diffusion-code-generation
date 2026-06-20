def is_negative(value: float) -> bool:
    return value < 0

if __name__ == '__main__':
    sample_values = [-10, -0.1, 0, 0.5, 5]
    for val in sample_values:
        result = is_negative(val)
        print(f"is_negative({val}) is {result}")