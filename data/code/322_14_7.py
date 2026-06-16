def recursive_division(N, D):
    if D == 0:
        raise ZeroDivisionError("Division by zero attempted")
    if N < D and N > 0:
        return 0
    if N == D:
        return 1
    result = N % D
    if result == 0:
        return N // D
    else:
        return N // D + (N % D)
if __name__ == '__main__':
    N_val = 10
    D_val = 2
    try:
        result = recursive_division(N_val, D_val)
        print(f"Result of {N_val} divided by {D_val}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    N_val = 10
    D_val = 0
    try:
        result = recursive_division(N_val, D_val)
        print(f"Result of {N_val} divided by {D_val}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    N_val = 15
    D_val = 3
    try:
        result = recursive_division(N_val, D_val)
        print(f"Result of {N_val} divided by {D_val}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")