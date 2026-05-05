def calculate_total_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) == 3:
            h = int(parts[0])
            m = int(parts[1])
            s = int(parts[2])
            total_minutes = h * 60 + m + s
            return total_minutes
        else:
            raise ValueError("Incorrect number of time components")
    except ValueError:
        return "Error: Invalid time format"
    except Exception:
        return "Error: An unexpected error occurred"
if __name__ == '__main__':
    time1 = "1:30:00"
    time2 = "23:59:59"
    time3 = "10:20"
    time4 = "abc:def:ghi"
    time5 = "5:30:15"
    print(f"Time: {time1}, Total Minutes: {calculate_total_minutes(time1)}")
    print(f"Time: {time2}, Total Minutes: {calculate_total_minutes(time2)}")
    print(f"Time: {time3}, Total Minutes: {calculate_total_minutes(time3)}")
    print(f"Time: {time4}, Total Minutes: {calculate_total_minutes(time4)}")
    print(f"Time: {time5}, Total Minutes: {calculate_total_minutes(time5)}")