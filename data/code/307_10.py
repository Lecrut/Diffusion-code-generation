def repeat_action(func, iterable, n):
    results = []
    for _ in range(n):
        results.extend(func(iterable))
    return results
if __name__ == '__main__':
    def double(x):
        return x * 2
    numbers = [1, 2, 3]
    repetitions = 3
    output = repeat_action(double, numbers, repetitions)
    print(output)