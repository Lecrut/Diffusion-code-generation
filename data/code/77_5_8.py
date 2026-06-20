def time_to_minutes(func):

    def wrapper(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return func(hours * 60 + minutes)
    return wrapper

@time_to_minutes
def process_time(minutes):
    return minutes
if __name__ == '__main__':
    print(process_time('1:30'))