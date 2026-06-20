import calendar

def format_date_string(date_string):
    month_names = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    
    try:
        year, month, day = date_string.split('-')
        formatted_month = month_names[month]
        return f"{formatted_month} {day}, {year}"
    except (ValueError, KeyError):
        return "Invalid date format"

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "2022-12-01"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))