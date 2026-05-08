import datetime
def determine_day(date_string):
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.day
if __name__ == '__main__':
    date1 = "2023-10-27"
    day1 = determine_day(date1)
    print(f"The day for {date1} is: {day1}")
    date2 = "1999-01-01"
    day2 = determine_day(date2)
    print(f"The day for {date2} is: {day2}")
    date3 = "2024-02-29"
    day3 = determine_day(date3)
    print(f"The day for {date3} is: {day3}")