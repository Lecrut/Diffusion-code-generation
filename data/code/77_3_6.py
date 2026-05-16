def calculate_total_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Incorrect number of time components")
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        if h < 0 or m < 0 or s < 0:
            raise ValueError("Time components cannot be negative")
        total_minutes = h * 60 + m + s
        return total_minutes
    except ValueError:
        return "Error: Invalid time format"
if __name__ == '__main__':
    time1 = "1:30:00"
    time2 = "23:59:59"
    time3 = "10:7:30"
    time4 = "1:30"
    time5 = "abc:def:ghi"
    time6 = "5:60:0"
    print(f"Time: {time1}, Total Minutes: {calculate_total_minutes(time1)}")
    print(f"Time: {time2}, Total Minutes: {calculate_total_minutes(time2)}")
    print(f"Time: {time3}, Total Minutes: {calculate_total_minutes(time3)}")
    print(f"Time: {time4}, Total Minutes: {calculate_total_minutes(time4)}")
    print(f"Time: {time5}, Total Minutes: {calculate_total_minutes(time5)}")
    print(f"Time: {time6}, Total Minutes: {calculate_total_minutes(time6)}")