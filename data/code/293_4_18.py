def time_converter(seconds):
    units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800}
    for unit, factor in units.items():
        if seconds % factor == 0:
            return f'{seconds // factor} {unit}'
    return 'Invalid time'
if __name__ == '__main__':
    print(time_converter(3600))
    print(time_converter(7 * 86400))