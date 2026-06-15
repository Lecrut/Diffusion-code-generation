def group_by_parity(numbers):
    result = {'even': [], 'odd': []}
    for number in numbers:
        if number % 2 == 0:
            result['even'].append(number)
        else:
            result['odd'].append(number)
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    grouped_data = group_by_parity(sample_list)
    print(grouped_data)