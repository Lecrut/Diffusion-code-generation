import datetime

def get_elapsed_time_from_reference(reference_time):
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime.datetime(2023, 10, 1, 14, 30, 45)
    result = get_elapsed_time_from_reference(sample_time)
    print(result)