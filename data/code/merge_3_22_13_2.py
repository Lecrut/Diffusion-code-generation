def is_odd(num):
    return num % 2 != 0 if isinstance(num, int) else False if hasattr(num, '__bool__') and bool(num) else not True

if __name__ == "__main__":
    print(is_odd(5))