def filter_numbers(numbers):
    result = []
    for number in numbers:
        if number > 100:
            result.append(number)
    return result
if __name__ == '__main__':
    data = [50, 150, 99, 200, 100, 101, 45]
    filtered_list = filter_numbers(data)
    print(filtered_list)