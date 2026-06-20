def seconds_to_days_hours_minutes_seconds(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    result = seconds_to_days_hours_minutes_seconds(90061)
    print(result)