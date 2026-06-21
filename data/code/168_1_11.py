def categorize_numbers(numbers):
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return {'even': even, 'odd': odd}

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    categorized = categorize_numbers(sample_numbers)
    print(categorized)