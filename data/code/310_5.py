def alternate_print(func1, func2):
    results = []
    for _ in range(3):
        result1 = func1()
        result2 = func2()
        print(f"Result of func1: {result1}")
        print(f"Result of func2: {result2}")
        results.append((result1, result2))
if __name__ == '__main__':
    def func_a():
        return "A"
    def func_b():
        return "B"
    alternate_print(func_a, func_b)