def conditional_execution(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(conditions):
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
@conditional_execution(True, "debug_mode")
def process_data(data, mode):
    return f"Processing data: {data} in {mode} mode"
@conditional_execution(False, "strict")
def process_data_strict(data, mode):
    return f"Processing data strictly: {data} in {mode} mode"
if __name__ == '__main__':
    print(process_data(100, "fast"))
    print(process_data(200, "fast"))
    print(process_data(300, "slow"))
    print(process_data_strict(400, "strict"))
    print(process_data_strict(500, "strict"))