def time_difference(hour1, minute1, hour2, minute2):
    total_minutes1 = hour1 * 60 + minute1
    total_minutes2 = hour2 * 60 + minute2
    
    if total_minutes2 < total_minutes1:
        total_minutes2 += 24 * 60
    
    difference_in_minutes = total_minutes2 - total_minutes1
    difference_in_hours = difference_in_minutes / 60
    
    return difference_in_hours

if __name__ == '__main__':
    print(time_difference(12, 0, 19, 30))