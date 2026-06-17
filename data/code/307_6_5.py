def repeated_action(func, n, start_value):
    current_value = start_value
    for i in range(n):
        result = func(current_value)
        print(f"Iteration {i + 1}: {func.__name__}({current_value}) = {result}")
        current_value = result
    return current_value
def example_function(x):
    return x * 2
if __name__ == '__main__':
    N = 5
    initial_val = 1
    print("Starting repeated action demonstration:")
    final_result = repeated_action(example_function, N, initial_val)
    print("\nRepetition finished. Final result:", final_result)