from datetime import datetime

def calculate_elapsed_hours(start_time, end_time):
    time_difference = end_time - start_time
    elapsed_hours = time_difference.total_seconds() / 3600.0
    return elapsed_hours

if __name__ == '__main__':
    sample_times = {
        'start': datetime(2023, 1, 1, 10, 0, 0),
        'end': datetime(2023, 1, 3, 14, 30, 0)
    }
    result = calculate_elapsed_hours(sample_times['start'], sample_times['end'])
    print(result)