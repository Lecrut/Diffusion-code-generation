def time_diff_to_milliseconds(time_str1: str, time_str2: str) -> int:
    hours1, minutes1, seconds1 = map(int, time_str1.split(':'))
    hours2, minutes2, seconds2 = map(int, time_str2.split(':'))
    
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    
    diff_seconds = abs(total_seconds2 - total_seconds1)
    return diff_seconds * 1000

if __name__ == '__main__':
    time_str1 = "14:35:45"
    time_str2 = "22:48:10"
    print(time_diff_to_milliseconds(time_str1, time_str2))