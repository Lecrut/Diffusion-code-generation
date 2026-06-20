def time_to_seconds(time_string):
    parts = time_string.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format. Expected H:M:S.")
    
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '0:0:0', '2:45:10', '10:5:5']
    for time_input in sample_times:
        result = time_to_seconds(time_input)
        print(result)