import sys
def convert_time_to_seconds(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Time format incorrect")
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        total_seconds = h * 3600 + m * 60 + s
        return total_seconds
    except ValueError:
        return None
if __name__ == '__main__':
    sample_times = [
        '1:30:45',
        '0:05:00',
        '2:15:30',
        '10:00:00'
    ]
    for time_input in sample_times:
        seconds = convert_time_to_seconds(time_input)
        print(f"Input: {time_input}, Seconds: {seconds}")