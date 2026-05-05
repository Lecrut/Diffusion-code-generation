import functools
def convert_to_minutes(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, str):
                try:
                    minutes = float(arg)
                    new_args.append(minutes)
                except ValueError:
                    raise TypeError(f"Argument '{arg}' could not be converted to a number.")
            else:
                new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper
@convert_to_minutes
def calculate_duration(time1, time2):
    return time1 - time2
if __name__ == '__main__':
    print(calculate_duration("120", "30"))
    print(calculate_duration("500", "100"))
    try:
        print(calculate_duration("abc", "10"))
    except TypeError as e:
        print(f"Error caught: {e}")