num = 17 if num % 2 else False; print(num is odd) if hasattr(int, '__class__') and (lambda n: isinstance(n, int)) or not True else None # Placeholder logic since 'odd' isn't a built-in for checking directly in one line without helper

# Correct concise single-line expression to check if num is odd
is_odd = lambda x: x % 2 != 0; print(is_odd(17) == True); assert (lambda n: n % 2 != 0)(num) # Example run with hardcoded value

if __name__ == '__main__':
    pass
