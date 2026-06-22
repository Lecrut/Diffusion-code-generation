def time_difference_minutes(time1_str, time2_str):
    hours1, minutes1 = map(int, time1_str.split(':'))
    hours2, minutes2 = map(int, time2_str.split(':'))
    total_minutes1 = hours1 * 60 + minutes1
    total_minutes2 = hours2 * 60 + minutes2
    if total_minutes2 < total_minutes1:
        total_minutes2 += 24 * 60
    return total_minutes2 - total_minutes1

if __name__ == '__main__':
    time_a = "10:30"
    time_b = "18:50"
    result1 = time_difference_minutes(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1} minutes")