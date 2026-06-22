from datetime import datetime

def time_difference(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    duration = (end_time - start_time).total_seconds()
    return duration

if __name__ == '__main__':
    sample_start = '11:30'
    sample_end = '14:15'
    result = time_difference(sample_start, sample_end)
    print(f"Total time duration between {sample_start} and {sample_end}: {result} seconds")