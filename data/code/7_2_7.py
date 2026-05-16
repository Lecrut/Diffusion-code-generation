import sys
def convert_time_to_seconds(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Time format incorrect")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        return total_seconds
    except ValueError:
        return None
if __name__ == '__main__':
    sample_times = [
        '1:30:45',
        '0:05:00',
        '2:15:30',
        '10:0:0',
        '30:30:30'
    ]
    for time_str in sample_times:
        seconds = convert_time_to_seconds(time_str)
        print(f"Input: {time_str}, Total Seconds: {seconds}")