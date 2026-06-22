def hours_to_minutes_seconds(hours):
    minutes = int(hours * 60)
    seconds = int(hours * 3600) % 60
    return f'{int(hours):02}:{minutes:02}:{seconds:02}'

if __name__ == '__main__':
    print(hours_to_minutes_seconds(1))
    print(hours_to_minutes_seconds(2.5))