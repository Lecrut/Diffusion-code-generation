time_conversion = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800}

def convert_time(value, from_unit, to_unit):
    return value * time_conversion[from_unit] / time_conversion[to_unit]
if __name__ == '__main__':
    print(convert_time(1, 'hours', 'minutes'))
    print(convert_time(24, 'hours', 'days'))
    print(convert_time(7, 'weeks', 'days'))