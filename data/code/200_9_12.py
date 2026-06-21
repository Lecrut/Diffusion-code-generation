def unique_values(numbers):
    return set(dict.fromkeys(numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 2, 3, 4, 4, 5]
    print(unique_values(sample_numbers))