def convert_to_minutes(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    return (hours * 60) + minutes + (seconds / 60.0)

if __name__ == '__main__':
    sample_duration = '1:30:00'
    total_minutes = convert_to_minutes(sample_duration)
    print(f"Duration: {sample_duration}")
    print(f"Total minutes: {total_minutes:.2f}")