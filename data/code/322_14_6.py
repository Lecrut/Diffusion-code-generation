def recursive_division(N, D):
    if D == 0:
        raise ZeroDivisionError("Division by zero attempted")
    if N == 0:
        return 0
    if N < D:
        return 0
    return recursive_division(D, N - D)
if __name__ == '__main__':
    N_val = 10
    D_val = 3
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val}: {result}")
    N_val = 12
    D_val = 4
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val}: {result}")
    N_val = 5
    D_val = 0
    try:
        result = recursive_division(N_val, D_val)
        print(f"Result of {N_val} divided by {D_val}: {result}")
    except ZeroDivisionError as e:
        print(f"Caught exception for {N_val} divided by {D_val}: {e}")