def convert_seconds(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError('Input must be a non-negative integer.')
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    remaining_seconds = seconds % 60
    return f'{hours}h {minutes}m {remaining_seconds}s'
if __name__ == '__main__':
    print(convert_seconds(3661))
    print(convert_seconds(7200))
    print(convert_seconds(45))