def find_max(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_values = [1, 5, 2, 8, 3], [-10, -5, -20, -1], [42]
    for values in sample_values:
        print(f"Max of {values}: {find_max(values)}")