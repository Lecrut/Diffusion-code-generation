def get_odd_numbers(numbers):
    odd_list = []
    for num in numbers:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

if __name__ == '__main__':
    sample_data = [15, 22, 37, 48, 53, 60, 79, 82, 91, 100]
    result = get_odd_numbers(sample_data)
    print(result)