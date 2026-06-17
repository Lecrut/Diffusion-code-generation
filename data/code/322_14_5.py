def recursive_division(N, D):
    if D == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if N == 0:
        return 0
    if N < D:
        return 0
    return recursive_division(N - D, D) + 1
if __name__ == '__main__':
    N_val = 10
    D_val = 3
    result = recursive_division(N_val, D_val)
    print(f"The result of dividing {N_val} by {D_val} is: {result}")
    N_val = 12
    D_val = 4
    result = recursive_division(N_val, D_val)
    print(f"The result of dividing {N_val} by {D_val} is: {result}")
    try:
        recursive_division(5, 0)
    except ZeroDivisionError as e:
        print(f"Caught exception: {e}")