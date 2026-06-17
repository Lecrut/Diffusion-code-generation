from datetime import datetime
def calculate_time_difference(time_str1, time_str2):
    try:
        format_str = '%H:%M:%S'
        time1 = datetime.strptime(time_str1, format_str)
        time2 = datetime.strptime(time_str2, format_str)
        return abs(time1 - time2)
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")
if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "05:30:45"
    try:
        difference = calculate_time_difference(time_a, time_b)
        print(f"Time A: {time_a}")
        print(f"Time B: {time_b}")
        print(f"Difference: {difference}")
    except ValueError as e:
        print(f"Error: {e}")
    time_c = "23:59:59"
    time_d = "00:00:01"
    try:
        difference2 = calculate_time_difference(time_c, time_d)
        print(f"\nTime C: {time_c}")
        print(f"Time D: {time_d}")
        print(f"Difference: {difference2}")
    except ValueError as e:
        print(f"Error: {e}")
    time_e = "10:15:30"
    time_f = "10:15:30"
    try:
        difference3 = calculate_time_difference(time_e, time_f)
        print(f"\nTime E: {time_e}")
        print(f"Time F: {time_f}")
        print(f"Difference: {difference3}")
    except ValueError as e:
        print(f"Error: {e}")