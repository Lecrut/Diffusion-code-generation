def convert_duration_to_minutes(duration_str):
    time_parts = duration_str.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes

if __name__ == '__main__':
    sample_duration = '1:30:00'
    total_minutes = convert_duration_to_minutes(sample_duration)
    print(f"Duration: {sample_duration}")
    print(f"Total minutes: {total_minutes:.2f}")