import datetime

def sort_dates_desc(date_strings):
    date_objects = []
    for date_str in date_strings:
        try:
            date_objects.append(datetime.datetime.strptime(date_str, "%Y-%m-%d"))
        except ValueError:
            print(f"Error parsing date: {date_str}")
    date_objects.sort(reverse=True)
    return [dt.strftime("%Y-%m-%d") for dt in date_objects]

if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2022-11-15",
        "2024-01-01",
        "2023-05-10"
    ]
    sorted_dates = sort_dates_desc(sample_dates)
    print("Sorted Dates:")
    for date in sorted_dates:
        print(date)