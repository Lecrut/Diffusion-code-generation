def repeat_n_times(action, n):
    for _ in range(n):
        yield action()
if __name__ == '__main__':
    def increment():
        return 1
    print("Testing repeat_n_times with increment repeated 3 times:")
    results = list(repeat_n_times(increment, 3))
    print(results)
    print("\nTesting repeat_n_times with a function that returns a value repeated 5 times:")
    def get_value():
        return "hello"
    results2 = list(repeat_n_times(get_value, 5))
    print(results2)