def odd_numbers(numbers):
    return (num for num in numbers if num % 2 != 0)
if __name__ == '__main__':
    data = [10, 35, 48, 79, 100, 121]
    result_list = list(odd_numbers(data))
    print(result_list)