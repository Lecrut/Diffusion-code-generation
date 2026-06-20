import datetime

def format_date(date_str):
    MONTHS = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
    }
    
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day = date_obj.day
    month = MONTHS[date_obj.month]
    year = date_obj.year
    
    return f"{day} {month} {year}"

if __name__ == '__main__':
    sample_date = "2022-11-11"
    result = format_date(sample_date)
    print(result)