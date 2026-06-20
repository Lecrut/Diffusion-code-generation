def filter_numbers(numbers, conditions):
    result = []
    for num in numbers:
        if all(condition(num) for condition in conditions):
            result.append(num)
    return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    conditions_a = lambda x: x % 2 == 0
    conditions_b = lambda x: x > 5
    filtered_list = filter_numbers(data, [conditions_a, conditions_b])
    print(filtered_list)