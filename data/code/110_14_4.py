from datetime import datetime
if __name__ == '__main__':
    date_strings = [
        "2023-10-26",
        "2022-11-15",
        "2023-01-01",
        "2022-12-31"
    ]
    date_objects = []
    for date_str in date_strings:
        try:
            date_objects.append(datetime.strptime(date_str, "%Y-%m-%d"))
        except ValueError:
            print(f"Error parsing date: {date_str}")
    date_objects.sort()
    print("Sorted Dates:")
    for date in date_objects:
        print(date.strftime("%Y-%m-%d"))