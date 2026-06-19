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
    sample_values = [0, 1, 2, 3, 4, 5, 10, 15]
    
    print("Recursive approach:")
    for value in sample_values:
        print(f"{value}: {is_even_recursive(value)}")
    
    print("\nDirect approach:")
    for value in sample_values:
        print(f"{value}: {is_even_direct(value)}")