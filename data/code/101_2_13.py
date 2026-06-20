def day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year % 100
    b = year // 100
    c = (a + (a//4) + ((b//4)*5) + ((b%4)*2) + day + (month*3)) % 7
    return ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][c]

if __name__ == '__main__':
    print(day_of_week(2024, 2, 29))