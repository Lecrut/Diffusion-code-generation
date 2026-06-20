def convert_to_total_minutes(time_str: str) -> int:
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

if __name__ == '__main__':
    time1 = "01:30"
    result1 = convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")

    time2 = "23:59"
    result2 = convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {result2}")