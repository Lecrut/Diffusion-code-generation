def time_difference_in_hours(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    if time2 < time1:
        h2 += 24
    
    total_minutes = (h2 - h1) * 60 + (m2 - m1)
    hours_difference = total_minutes / 60
    return hours_difference

if __name__ == '__main__':
    print(time_difference_in_hours('12:00', '19:30'))
    print(time_difference_in_hours('19:30', '12:00'))