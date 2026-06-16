def apply_predicate(predicate, data):
    result = True if len(data) > 0 else False
    for item in data:
        if not predicate(item):
            return False
    return result
if __name__ == '__main__':
    def is_even(n):
        return n % 2 == 0
    numbers = [1, 2, 3, 4, 5]
    print(apply_predicate(is_even, numbers))