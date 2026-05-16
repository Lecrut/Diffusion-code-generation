import datetime
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2022-12-01"
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        if date1 > date2:
            difference = (date1 - date2).days
        else:
            difference = (date2 - date1).days
        print(difference)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")