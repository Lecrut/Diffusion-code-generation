def filter_sort_integers(numbers):
    return sorted(int(num) for num in numbers if num > 0)

if __name__ == '__main__':
    sample_values = [-2.5, 3.14, -7.89, 0.0, 5.6]
    result = filter_sort_integers(sample_values)
    print(result)