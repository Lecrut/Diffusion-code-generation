conversion_factors = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800
}

def time_converter(value, from_unit, to_unit):
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

if __name__ == '__main__':
    seconds = 3600
    minutes = time_converter(seconds, 'seconds', 'minutes')
    print(f"{seconds} seconds is {minutes:.2f} minutes")

    days = 7
    hours = time_converter(days, 'days', 'hours')
    print(f"{days} days is {hours:.2f} hours")

    weeks = 1
    seconds = time_converter(weeks, 'weeks', 'seconds')
    print(f"{weeks} weeks is {seconds:.2f} seconds")