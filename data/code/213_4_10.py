def sort_descending(numbers):
    return sorted(numbers, key=lambda x: -x)

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, 2.9, 0.7]
    sorted_numbers = sort_descending(sample_numbers)
    print(sorted_numbers)