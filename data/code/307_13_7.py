def repeat_n_times(action, n):
    for _ in range(n):
        yield action()
if __name__ == '__main__':
    def increment():
        return 1
    result_generator = repeat_n_times(increment, 5)
    results = list(result_generator)
    print(results)