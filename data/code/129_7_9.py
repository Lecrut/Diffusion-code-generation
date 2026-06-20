def filter_sort_integers(numbers):
    return sorted(int(num) for num in numbers if num > 0)

if __name__ == '__main__':
    sample_numbers = [3.5, -2.1, 4.8, 0, -1.7, 6.0]
    print(filter_sort_integers(sample_numbers))