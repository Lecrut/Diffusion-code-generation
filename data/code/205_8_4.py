def convert_and_sort(numbers):
    return sorted(map(float, numbers))

if __name__ == '__main__':
    sample_values = ['10', 2.5, '3.14', 7]
    sorted_numbers = convert_and_sort(sample_values)
    print(sorted_numbers)