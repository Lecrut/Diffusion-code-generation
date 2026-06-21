def categorize_numbers(numbers):
    even = []
    odd = []
    for num in numbers:
        if isinstance(num, int):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
    return {'even': even, 'odd': odd}

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    categorized = categorize_numbers(sample_numbers)
    print(categorized)