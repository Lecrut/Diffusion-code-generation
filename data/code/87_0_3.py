def combine_conditions(numbers, condition_a, condition_b):
    result = []
    for num in numbers:
        if num > condition_a and num < condition_b:
            result.append(num)
    return result
if __name__ == '__main__':
    data = [1, 5, 10, 15, 20, 25, 30]
    lower_bound = 4
    upper_bound = 22
    filtered_numbers = combine_conditions(data, lower_bound, upper_bound)
    print(filtered_numbers)