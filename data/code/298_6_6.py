def time_difference_in_minutes(time1, time2):
    hours1, minutes1 = map(int, time1.split(':'))
    hours2, minutes2 = map(int, time2.split(':'))
    
    total_minutes1 = hours1 * 60 + minutes1
    total_minutes2 = hours2 * 60 + minutes2
    
    diff = total_minutes2 - total_minutes1
    return diff if diff >= 0 else -diff

if __name__ == '__main__':
    time_a = '18:30'
    time_b = '07:45'
    difference = time_difference_in_minutes(time_a, time_b)
    print(difference)