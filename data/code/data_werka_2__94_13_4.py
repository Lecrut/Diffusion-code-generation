def any_satisfies(sequence, predicate):
    for item in sequence:
        if predicate(item):
            return True
    return False

if __name__ == '__main__':
    numbers = [0, 0, 0, 1, 0]
    result = any_satisfies(numbers, lambda x: x > 0)
    print(result)