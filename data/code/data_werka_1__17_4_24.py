def is_even_recursive(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_recursive(n - 2)

def is_even_modulo(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 10, 15, 20]
    for value in test_values:
        print(f"Recursive: {value} is even: {is_even_recursive(value)}")
        print(f"Modulo: {value} is even: {is_even_modulo(value)}")