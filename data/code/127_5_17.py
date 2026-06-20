def filter_odds(numbers):
    return (num for num in numbers if num % 2 != 0)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_generator = filter_odds(sample_numbers)
    result = list(odd_generator)
    print(result)