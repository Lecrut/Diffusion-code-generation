def time_difference(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    if time2 < time1:
        return -(60 * (h2 - h1) + (m2 - m1))
    else:
        return 60 * (h2 - h1) + (m2 - m1)

if __name__ == '__main__':
    result = time_difference('08:15', '20:45')
    print(result)