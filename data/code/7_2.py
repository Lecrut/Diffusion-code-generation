def time_to_seconds(time_str):
    parts = time_str.split(':')
    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])
    total = h * 3600 + m * 60 + s
    return total

if __name__ == '__main__':
    result = time_to_seconds('1:30:45')
    print(result)