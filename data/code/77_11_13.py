def time_to_minutes(time_str):
    try:
        h, m = map(int, time_str.split(':')[:2])
        return h * 60 + m
    except ValueError:
        raise ValueError("Invalid time format. Expected 'HH:MM'.")

if __name__ == '__main__':
    test_times = [
        "00:00",
        "01:30",
        "23:59"
    ]
    
    for time_str in test_times:
        try:
            print(f"{time_str} -> {time_to_minutes(time_str)} minutes")
        except ValueError as e:
            print(e)