def extract_odds(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 11, 13, 15]
    odd_numbers = extract_odds(sample_values)
    print(odd_numbers)