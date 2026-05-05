import calendar
if __name__ == '__main__':
    month1 = "January"
    month2 = "March"
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    if month1 in month_map and month2 in month_map:
        num1 = month_map[month1]
        num2 = month_map[month2]
        if num1 < num2:
            difference = num2 - num1
        else:
            difference = num1 - num2
        print(difference)
    else:
        print("Invalid month input")