def is_positive_and_less_than_100(value):
    return value > 0 and value < 100

if __name__ == '__main__':
    sample_values = [50, -10, 100, 1, 99]
    for val in sample_values:
        print(f"is_positive_and_less_than_100({val}) is: {is_positive_and_less_than_100(val)}")