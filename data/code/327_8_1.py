def apply_operation(numbers):
    return [numbers[0] * x for x in numbers[1:]]
if __name__ == '__main__':
    data = [2, 3, 4, 5]
    result = apply_operation(data)
    print(result)