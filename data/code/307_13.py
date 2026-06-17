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
    def get_square():
        return 4
    print("\nTesting repeat_n_times with get_square repeated 2 times:")
    results_two = list(repeat_n_times(get_square, 2))
    print(results_two)