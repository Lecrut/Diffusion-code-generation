def collect_odd_numbers(data):
    odd_numbers = []
    for number in data:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = collect_odd_numbers(sample_list)
    print(result)