def categorize_numbers(strings):
    even = []
    odd = []
    for s in strings:
        num = int(s)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {'even': even, 'odd': odd}

if __name__ == '__main__':
    sample_values = ['1', '2', '3', '4', '5', '6']
    result = categorize_numbers(sample_values)
    print(result)