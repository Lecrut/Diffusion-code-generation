def any_satisfies(sequence, condition):
    for item in sequence:
        if condition(item):
            return True
    return False

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = any_satisfies(numbers, lambda x: x > 3)
    print(result)