import datetime
def format_date_with_month(date_str: str) -> str:
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format"
    year = dt.year
    month_num = dt.month
    day = dt.day
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return f"{year}-{months[month_num]}-{day}"
if __name__ == '__main__':
    sample_dates = ["2023-10-15", "2024-06-01", "2020-12-31"]
    for date_str in sample_dates:
        formatted_date = format_date_with_month(date_str)
        print(formatted_date)