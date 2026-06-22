def find_min_max(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_numbers = "10,20,30,40,50"
    print(find_min_max(sample_numbers))