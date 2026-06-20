def time_to_minutes(time_str):
    time_format = "%H:%M:%S"
    try:
        total_seconds = int(datetime.strptime(time_str, time_format).strftime("%s"))
        return total_seconds // 60
    except ValueError:
        return None

if __name__ == '__main__':
    sample_time = "12:34:56"
    result = time_to_minutes(sample_time)
    print(result)