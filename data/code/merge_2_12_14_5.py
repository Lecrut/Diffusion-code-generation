def get_odd_numbers(numbers):
    return (num for num in numbers if num % 2 != 0)
if __name__ == '__main__':
    data = [1, 4, 7, 8, 9, 12]
    odd_gen = get_odd_numbers(data)
    result_list = list(odd_gen)
    print(result_list)