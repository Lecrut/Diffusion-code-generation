def time_difference(time1, time2):
    hour1, min1 = map(int, time1.split(':'))
    hour2, min2 = map(int, time2.split(':'))

    total_min1 = hour1 * 60 + min1
    total_min2 = hour2 * 60 + min2

    return total_min2 - total_min1 if total_min2 >= total_min1 else -(total_min1 - total_min2)

if __name__ == '__main__':
    difference = time_difference('08:15', '20:45')
    print(difference)