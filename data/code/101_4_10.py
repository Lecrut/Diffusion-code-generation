def day_of_week(date_str):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year, month, day = map(int, date_str.split('-'))
    
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    h = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    
    return weekdays[h]

if __name__ == '__main__':
    date_str = "2023-04-10"
    print(day_of_week(date_str))