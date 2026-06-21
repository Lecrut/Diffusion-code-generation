def unique_ordered_values(numbers):
    return set(dict.fromkeys(numbers))

if __name__ == '__main__':
    sample_numbers = [4, 5, 6, 4, 3, 2, 1, 5]
    print(unique_ordered_values(sample_numbers))