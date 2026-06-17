def recursive_division(N, D):
    if D == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if N < D:
        return 0
    else:
        return N % D
if __name__ == '__main__':
    N_val = 10
    D_val = 2
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val}: {result}")
    N_val = 10
    D_val = 0
    try:
        result = recursive_division(N_val, D_val)
        print(f"Result of {N_val} divided by {D_val}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    N_val = 5
    D_val = 8
    result = recursive_division(N_val, D_val)
    print(f"Result of {N_val} divided by {D_val}: {result}")