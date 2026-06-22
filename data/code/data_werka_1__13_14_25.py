def convert_seconds_to_dhms(total_seconds):
    days = total_seconds // (3600 * 24)
    hours = (total_seconds % (3600 * 24)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 987654
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")