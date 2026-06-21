def convert_to_minutes(days, hours, minutes, seconds):
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes + (seconds / 60)
    return total_minutes

if __name__ == '__main__':
    days = 1
    hours = 3
    minutes = 45
    seconds = 30
    result = convert_to_minutes(days, hours, minutes, seconds)
    print(result)