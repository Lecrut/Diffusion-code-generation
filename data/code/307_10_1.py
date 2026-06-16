def repeat_action(func, iterable, n):
    result = []
    for _ in range(n):
        result.extend(iterable)
    return result
if __name__ == '__main__':
    def add(a, b):
        return a + b
    numbers = [1, 2]
    repetitions = 3
    output = repeat_action(add, numbers, repetitions)
    print(output)