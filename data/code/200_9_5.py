def unique_values(numbers):
    return set(dict.fromkeys(numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(unique_values(sample_numbers))