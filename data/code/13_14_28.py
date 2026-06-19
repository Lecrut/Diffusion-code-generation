def convert_seconds(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 987654
    days, hours, minutes, seconds = convert_seconds(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")