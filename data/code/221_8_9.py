def order_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_values = [34, 7, 23]
    result = order_numbers(*sample_values)
    print(result)