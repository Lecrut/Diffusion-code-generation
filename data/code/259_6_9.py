def find_extremes(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = "10,20,30,40,50"
    print(find_extremes(sample_values))