def convert_hours_to_time(hours):
    minutes = hours * 60
    seconds = minutes * 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

if __name__ == '__main__':
    print(convert_hours_to_time(1))
    print(convert_hours_to_time(2.5))
    print(convert_hours_to_time(3.75))