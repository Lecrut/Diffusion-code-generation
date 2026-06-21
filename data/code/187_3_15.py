MAX_VALUE = float('-inf')

if __name__ == '__main__':
    sample_values = [10, 5, 20, 8, 15]
    largest_value = max(sample_values, default=MAX_VALUE)
    print(f"The largest value in {sample_values} is: {largest_value}")