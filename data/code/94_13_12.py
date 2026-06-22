def any_satisfies(sequence, condition):
    for item in sequence:
        if condition(item):
            return True
    return False

if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9, 10, 12]
    result = any_satisfies(numbers, lambda x: x > 10)
    print(result)