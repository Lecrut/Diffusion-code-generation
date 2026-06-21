def find_minimum(numbers):
    return min(numbers)

if __name__ == '__main__':
    sample_values = [45, 21, 89, 3, 77, 22]
    if not sample_values:
        print("Error: Input list is empty")
    else:
        smallest_value = find_minimum(sample_values)
        print(smallest_value)