def calculate_duration(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    total_minutes = (h2 - h1) * 60 + (m2 - m1)
    return abs(total_minutes)

if __name__ == '__main__':
    duration = calculate_duration('07:45', '18:23')
    print(duration)