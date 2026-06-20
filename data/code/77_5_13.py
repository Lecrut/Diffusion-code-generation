from functools import wraps

def time_to_minutes(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, str) and ':' in arg:
                hours, minutes = map(int, arg.split(':'))
                total_minutes = hours * 60 + minutes
                new_args.append(total_minutes)
            else:
                new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper

@time_to_minutes
def calculate_total_time(time1, time2):
    return time1 + time2
if __name__ == '__main__':
    print(calculate_total_time('1:30', '2:45'))