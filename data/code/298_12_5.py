class TimeCalculator:
    def difference(self, time1_str, time2_str):
        time1 = tuple(map(int, time1_str.split(':')))
        time2 = tuple(map(int, time2_str.split(':')))
        total_seconds1 = time1[0] * 3600 + time1[1] * 60 + time1[2]
        total_seconds2 = time2[0] * 3600 + time2[1] * 60 + time2[2]
        difference_seconds = abs(total_seconds1 - total_seconds2)
        hours = difference_seconds // 3600
        minutes = (difference_seconds % 3600) // 60
        seconds = difference_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    calculator = TimeCalculator()
    time_a = "01:00:00"
    time_b = "05:30:15"
    result = calculator.difference(time_a, time_b)
    print(result)
    time_c = "10:20:00"
    time_d = "09:00:00"
    result2 = calculator.difference(time_c, time_d)
    print(result2)
    time_e = "00:00:00"
    time_f = "23:59:59"
    result3 = calculator.difference(time_e, time_f)
    print(result3)