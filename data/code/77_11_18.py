def time_to_minutes(time_str):
    parts = time_str.split(':')
    h, m, s = map(int, parts)
    return h * 60 + m + (s / 60)

if __name__ == '__main__':
    print(time_to_minutes("00:00:00"))
    print(time_to_minutes("1:30:00"))