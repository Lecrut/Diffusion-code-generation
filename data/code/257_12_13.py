def find_difference(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num - min_num

if __name__ == '__main__':
    sample_numbers = (3.5, 7.2, 1.8, 9.4, 5.6)
    difference = find_difference(sample_numbers)
    print(difference)