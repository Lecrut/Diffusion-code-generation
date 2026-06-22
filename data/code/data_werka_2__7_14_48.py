def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    time_units = {
        'days': 24 * 60,
        'hours': 60,
        'minutes': 1,
        'seconds': 1 / 60
    }
    
    total_minutes = (days * time_units['days']) + \
                    (hours * time_units['hours']) + \
                    (minutes * time_units['minutes']) + \
                    (seconds * time_units['seconds'])
    
    return total_minutes

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 15
    sample_seconds = 30
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)