def time_difference(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    if h1 > h2:
        h2 += 24
    
    total_minutes = (h2 - h1) * 60 + (m2 - m1)
    return abs(total_minutes)

if __name__ == '__main__':
    print(time_difference('09:45', '23:15'))
    print(time_difference('23:15', '09:45'))