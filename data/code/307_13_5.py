def repeat_n_times(action, n):
    for _ in range(n):
        yield action()
if __name__ == '__main__':
    def increment():
        return 1
    n_value = 5
    result_generator = repeat_n_times(increment, n_value)
    print("Repeating increment function 5 times:")
    for i, result in enumerate(result_generator):
        print(f"Iteration {i+1}: {result}")