def time_difference(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    
    diff = total_minutes2 - total_minutes1
    
    return diff

if __name__ == '__main__':
    sample_time1 = '18:30'
    sample_time2 = '09:45'
    result = time_difference(sample_time1, sample_time2)
    print(result)