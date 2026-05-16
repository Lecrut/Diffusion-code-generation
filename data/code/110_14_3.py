import datetime
if __name__ == '__main__':
    date_strings = [
        "2023-10-26",
        "2022-01-15",
        "2024-05-01",
        "2023-03-10"
    ]
    date_objects = []
    for date_str in date_strings:
        try:
            date_objects.append(datetime.datetime.strptime(date_str, "%Y-%m-%d"))
        except ValueError:
            print(f"Error parsing date: {date_str}")
    date_objects.sort()
    print("Sorted Dates:")
    for dt in date_objects:
        print(dt.strftime("%Y-%m-%d"))