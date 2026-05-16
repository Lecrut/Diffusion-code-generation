import datetime
if __name__ == '__main__':
    date_strings = ["2023-10-26", "2023-01-15", "2024-05-01", "2023-11-30"]
    date_objects = []
    for date_str in date_strings:
        date_objects.append(datetime.datetime.strptime(date_str, "%Y-%m-%d"))
    date_objects.sort()
    sorted_date_strings = [dt.strftime("%Y-%m-%d") for dt in date_objects]
    print("Sorted Dates:")
    for date_str in sorted_date_strings:
        print(date_str)