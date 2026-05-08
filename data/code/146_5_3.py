def filter_numbers(numbers):
    result = []
    for number in numbers:
        if number > 100:
            result.append(number)
    return result
if __name__ == '__main__':
    data = [50, 101, 99, 150, 100, 200, 75]
    filtered = filter_numbers(data)
    print(filtered)