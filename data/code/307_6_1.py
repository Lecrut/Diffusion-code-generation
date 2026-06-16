def function_N(x):
    return x * 2
def repeat_function(func, n, initial_value):
    result = initial_value
    for i in range(n):
        result = func(result)
        print(f"Iteration {i+1}: Result is {result}")
    return result
if __name__ == '__main__':
    N_times = 3
    start_value = 5
    final_result = repeat_function(function_N, N_times, start_value)
    print(f"Final result after {N_times} repetitions: {final_result}")