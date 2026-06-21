def sort_descending(numbers):
    numbers.sort(key=lambda x: -x)
    return numbers

if __name__ == '__main__':
    sample_values = [5.6, 3.2, 7.8, 1.4, 0.9]
    sorted_values = sort_descending(sample_values)
    print(sorted_values)