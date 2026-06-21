def sort_descending(numbers):
    numbers.sort(key=lambda x: -x)
    return numbers

if __name__ == '__main__':
    sample_values = [5.1, 2.7, 3.4, 8.0, 1.9]
    sorted_values = sort_descending(sample_values)
    print(sorted_values)