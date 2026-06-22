EVEN_THRESHOLD = 2

def is_even_recursive(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_recursive(n - EVEN_THRESHOLD)

def is_even_modulo(n):
    return n % EVEN_THRESHOLD == 0

if __name__ == '__main__':
    sample_values = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    print("Recursive approach:")
    for value in sample_values:
        print(f"{value}: {is_even_recursive(value)}")
    print("\nModulo approach:")
    for value in sample_values:
        print(f"{value}: {is_even_modulo(value)}")