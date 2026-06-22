def convert_seconds_to_dhms(total_seconds):
    time_units = {
        'days': 3600 * 24,
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    
    days = total_seconds // time_units['days']
    remaining_seconds = total_seconds % time_units['days']
    
    hours = remaining_seconds // time_units['hours']
    remaining_seconds %= time_units['hours']
    
    minutes = remaining_seconds // time_units['minutes']
    seconds = remaining_seconds % time_units['minutes']
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")