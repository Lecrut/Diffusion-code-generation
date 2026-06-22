SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60

def convert_seconds_to_hms(seconds):
    hours = seconds // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)
    minutes = (seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)) // SECONDS_PER_MINUTE
    remaining_seconds = seconds % SECONDS_PER_MINUTE
    return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"

if __name__ == '__main__':
    print(convert_seconds_to_hms(3661))