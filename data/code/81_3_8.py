def calculate_time_difference(time1_str: str, time2_str: str) -> int:
    hours1, minutes1, seconds1 = map(int, time1_str.split(':'))
    hours2, minutes2, seconds2 = map(int, time2_str.split(':'))
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    if total_seconds2 < total_seconds1:
        total_seconds2 += 86400
    difference_in_seconds = abs(total_seconds2 - total_seconds1)
    difference_in_hours = difference_in_seconds // 3600
    return difference_in_hours
if __name__ == '__main__':
    start_time_str = '19:00:00'
    end_time_str = '07:30:00'
    elapsed = calculate_time_difference(start_time_str, end_time_str)
    print(f'{elapsed}')