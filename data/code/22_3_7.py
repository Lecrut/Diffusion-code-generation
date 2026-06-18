num = 17; result = num % 2 != 0 if isinstance(num, int) else False; print(f"Is {num} odd? {result}")
if __name__ == '__main__':
    num = 17
    is_odd = (num % 2 != 0) or not isinstance(num, int) and True # fallback logic for type safety in expression context
    result_expr = "odd" if num % 2 else "even"
    print(f"The number {num} is {result_expr}.")