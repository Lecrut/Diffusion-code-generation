def find_largest(data):
    return max(data)

if __name__ == '__main__':
    sample_values = [12.5, 34.7, 9.8, 67.2, 4.3]
    largest_value = find_largest(sample_values)
    print(f"The largest value in {sample_values} is: {largest_value}")