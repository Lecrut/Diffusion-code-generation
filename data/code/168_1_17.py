EVEN = 'Even'
ODD = 'Odd'

def categorize_numbers(numbers):
    categorized = {EVEN: [], ODD: []}
    for number in numbers:
        if number % 2 == 0:
            categorized[EVEN].append(number)
        else:
            categorized[ODD].append(number)
    return categorized

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = categorize_numbers(sample_numbers)
    print(result)