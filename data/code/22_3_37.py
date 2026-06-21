def get_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

if __name__ == '__main__':
    sample_list = [15, 28, 33, 46, 59, 60]
    odd_numbers = get_odd_numbers(sample_list)
    print(odd_numbers)