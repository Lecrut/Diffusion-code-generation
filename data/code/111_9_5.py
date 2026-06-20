def format_date(date):
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    day, month, year = map(int, date.split())
    return f"{day} {month_names[month-1]} {year}"

if __name__ == '__main__':
    print(format_date("11 11 2022"))