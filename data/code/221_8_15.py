def sort_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_a = 42
    sample_b = 15
    sample_c = 36
    result = sort_numbers(sample_a, sample_b, sample_c)
    print(result)