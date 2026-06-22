def time_difference(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    
    diff = total_minutes2 - total_minutes1
    
    if diff < 0:
        return -diff
    
    return diff

if __name__ == '__main__':
    time_a = '08:15'
    time_b = '20:45'
    difference = time_difference(time_a, time_b)
    print(difference)