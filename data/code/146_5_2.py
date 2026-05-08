def filter_numbers(numbers):
    result = []
    for number in numbers:
        if number > 100:
            result.append(number)
    return result
if __name__ == '__main__':
    sample_list = [50, 101, 99, 150, 100, 200, 100.5]
    filtered_list = filter_numbers(sample_list)
    print(filtered_list)