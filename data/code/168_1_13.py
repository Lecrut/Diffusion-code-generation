def categorize_numbers(numbers):
    categorized = {'even': [], 'odd': []}
    for number in numbers:
        if int(number) % 2 == 0:
            categorized['even'].append(int(number))
        else:
            categorized['odd'].append(int(number))
    return categorized

if __name__ == '__main__':
    sample_numbers = ['1', '2', '3', '4', '5', '6']
    result = categorize_numbers(sample_numbers)
    print(result)