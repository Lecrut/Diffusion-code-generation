def repeat_n_times(action, n):
    for _ in range(n):
        yield action()
if __name__ == '__main__':
    def increment():
        return 1
    print("Testing repeat_n_times with increment repeated 3 times:")
    results = list(repeat_n_times(increment, 3))
    print(results)
    print("\nTesting repeat_n_times with increment repeated 0 times:")
    results_zero = list(repeat_n_times(increment, 0))
    print(results_zero)
    def get_value():
        return 42
    print("\nTesting repeat_n_times with get_value repeated 5 times:")
    results_five = list(repeat_n_times(get_value, 5))
    print(results_five)