import re
TIME_PATTERN = re.compile('(\\d+):(\\d+):(\\d+)')

def time_to_minutes(duration_str):
    match = TIME_PATTERN.match(duration_str)
    if not match:
        raise ValueError('Invalid time format')
    hours, minutes, seconds = map(int, match.groups())
    return hours * 60 + minutes + seconds / 60

def decorator(func):

    def wrapper(*args, **kwargs):
        for i in range(len(args)):
            if isinstance(args[i], str) and TIME_PATTERN.match(args[i]):
                args = list(args)
                args[i] = time_to_minutes(args[i])
                break
        return func(*args, **kwargs)
    return wrapper

@decorator
def process_time(duration):
    return duration * 2
if __name__ == '__main__':
    result1 = process_time('1:30:00')
    print(result1)
    result2 = process_time('0:05:30')
    print(result2)
    result3 = process_time('2:0:0')
    print(result3)