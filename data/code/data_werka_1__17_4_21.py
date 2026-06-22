def is_even_recursive(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_recursive(n - 2)

def is_even_direct(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 10, 15, 20]
    results_recursive = {n: is_even_recursive(n) for n in sample_values}
    results_direct = {n: is_even_direct(n) for n in sample_values}

    print("Recursive Approach:")
    print(results_recursive)
    print("\nDirect Approach:")
    print(results_direct)