def is_negative(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [-10, 0, 5]
    for value in sample_values:
        result = is_negative(value)
        print(f"The number {value} is negative: {result}")