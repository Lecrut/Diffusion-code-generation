def repeated_function(func, n):
    for i in range(n):
        func(i)
def function_N(x):
    print(f"Calling function_N with value: {x}")
if __name__ == '__main__':
    repeated_function(function_N, 3)