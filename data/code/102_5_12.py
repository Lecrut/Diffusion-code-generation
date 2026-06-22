import datetime

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def find_weekdays(date_strings):
    results = []
    for ds in date_strings:
        dt = datetime.datetime.strptime(ds, "%Y-%m-%d")
        wd = dt.weekday()
        if wd < 5:
            results.append({
                "date": ds,
                "name": DAY_NAMES[wd]
            })
    return results

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    result = find_weekdays(sample_dates)
    print(result)