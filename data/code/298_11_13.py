if __name__ == '__main__':
    time1 = '14:30'
    time2 = '16:45'

    def parse_time(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60

    time_difference_seconds = abs(parse_time(time2) - parse_time(time1))
    print(time_difference_seconds)