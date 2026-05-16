def condition_decorator(condition1, condition2=None, **kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition1:
                return func(*args, **kwargs)
            elif condition2:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
@condition_decorator(True)
def execute_task(a, b):
    return a + b
@condition_decorator(False, True)
def execute_task_conditional(a, b):
    return a * b
if __name__ == '__main__':
    print(execute_task(5, 3))
    print(execute_task_conditional(5, 3))