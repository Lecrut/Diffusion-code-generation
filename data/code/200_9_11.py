def unique_ordered_values(numbers):
    return dict.fromkeys(numbers).keys()

if __name__ == '__main__':
    sample_numbers = [4, 5, 6, 5, 4, 3, 2, 1]
    print(list(unique_ordered_values(sample_numbers)))