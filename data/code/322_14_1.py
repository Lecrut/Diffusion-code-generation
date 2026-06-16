def recursive_division(N, D):
    if D == 0:
        raise ZeroDivisionError("Division by zero attempted")
    if N == 0:
        return 0
    if N < D:
        return 0
    return recursive_division(N - D, D) + 1
if __name__ == '__main__':
    N_val = 10
    D_val = 3
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val} (using repeated subtraction logic): {result}")
    N_val = 10
    D_val = 0
    try:
        recursive_division(N_val, D_val)
    except ZeroDivisionError as e:
        print(f"Caught exception for division by zero: {e}")
    N_val = 5
    D_val = 2
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val} (using repeated subtraction logic): {result}")