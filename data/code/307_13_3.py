def repeat_n_times(action, n):
    for _ in range(n):
        yield action()
if __name__ == '__main__':
    def greet():
        return "Hello"
    print("Testing repeat_n_times with 3 repetitions:")
    results1 = list(repeat_n_times(greet, 3))
    print(results1)
    print("\nTesting repeat_n_times with 5 repetitions:")
    results2 = list(repeat_n_times(greet, 5))
    print(results2)