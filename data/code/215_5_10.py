def find_highest_value(numbers):
    return max(numbers, key=lambda x: x)

if __name__ == '__main__':
    sample_values = [-5, -10, -2, -8, -1]
    highest_value = find_highest_value(sample_values)
    print(highest_value)