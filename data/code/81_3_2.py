def time_difference(time1: str, time2: str) -> int:
    hours1, minutes1, seconds1 = map(int, time1.split(':'))
    hours2, minutes2, seconds2 = map(int, time2.split(':'))
    
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    
    difference_in_seconds = abs(total_seconds2 - total_seconds1)
    difference_in_hours = difference_in_seconds // 3600
    
    return difference_in_hours

if __name__ == '__main__':
    print(time_difference('09:00:00', '17:30:00'))