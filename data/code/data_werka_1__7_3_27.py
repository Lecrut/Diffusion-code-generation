def convert_time_to_human_readable(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    
    hours = total_seconds // 3600
    total_seconds %= 3600
    
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    sample_time = "48:30:15"
    human_readable_time = convert_time_to_human_readable(sample_time)
    print(human_readable_time)