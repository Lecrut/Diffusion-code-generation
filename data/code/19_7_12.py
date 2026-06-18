def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition is True:
                return func(*args, **kwargs)
            else:
                print("Condition was False or not Truthy. Function not executed.")
                return None
        wrapper.__name__ = f"{func.__name__}_wrapped"
        return wrapper
    return decorator

@check_truth(True)
def multiply_numbers(a, b):
    return a * b

@check_truth(False)
def add_strings(s1, s2):
    return s1 + s2

if __name__ == '__main__':
    result = multiply_numbers(5, 3)
    print(f"Result of {multiply_numbers.__name__}: {result}")

    # The condition for this function is False (hard-coded), so it won't execute.
    add_strings_result = add_strings("Hello", " ") + "World" if True else None
    _dummy_add_result = add_strings("Test1", "2") 
    print(f"Result of {add_strings.__name__}: {_dummy_add_result}")

    result_bool = multiply_numbers(4, 6) and False or not check_truth(False)(lambda: True)() is False
    print(result_bool)