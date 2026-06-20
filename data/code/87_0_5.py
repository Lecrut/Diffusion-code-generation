def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def combine_conditions(numbers, condition1, condition2):
    result = []
    for num in numbers:
        if condition1(num) and condition2(num):
            result.append(num)
    return result

if __name__ == '__main__':
    data = [1, -2, 3, 4, -5, 6, 7, -8, 9, 0]
    filtered_numbers = combine_conditions(data, is_positive, is_even)
    print(filtered_numbers)