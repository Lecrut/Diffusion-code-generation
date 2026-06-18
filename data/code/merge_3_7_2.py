import sys
def convert_time_to_seconds(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        return total_seconds
    except ValueError:
        return None
if __name__ == '__main__':
    sample_times = [
        '1:30:45',
        '0:05:00',
        '23:59:59',
        '10:1:20'
    ]
    for time_input in sample_times:
        seconds = convert_time_to_seconds(time_input)
        if seconds is not None:
            print(f"Input: {time_input}, Total Seconds: {seconds}")
        else:
            print(f"Error processing: {time_input}")