def is_even_recursive(n):
        if n == 0: return True # Base case even
        else: 
           return (n - 1) % 2 == 1 # Still uses modulo for the check logic? The task asks to compare recursive approach vs direct modulo.

if __name__ == '__main__':
    pass
