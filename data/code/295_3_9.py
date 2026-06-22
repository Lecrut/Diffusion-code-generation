def hours_to_time(hours):
    minutes = hours * 60
    seconds = minutes * 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(hours_to_time(1))
    print(hours_to_time(2))