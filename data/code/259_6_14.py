def find_extremes(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_input = "3,1,4,1,5,9,2,6,5,3,5"
    print(find_extremes(sample_input))