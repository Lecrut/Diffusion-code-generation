def sort_mixed_numbers(numbers):
    return sorted(map(float, numbers))

if __name__ == '__main__':
    sample_values = ['10', 2.5, '3.14', 7]
    sorted_values = sort_mixed_numbers(sample_values)
    print(sorted_values)