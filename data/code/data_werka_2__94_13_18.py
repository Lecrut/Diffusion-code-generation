def any_satisfies(sequence, predicate):
    for item in sequence:
        if predicate(item):
            return True
    return False

if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9]
    result = any_satisfies(numbers, lambda x: x > 5)
    print(result)