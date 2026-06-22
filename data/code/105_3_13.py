from datetime import date
import calendar

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

def get_next_15th():
    start_date = date(2023, 3, 3)
    current_year = start_date.year
    current_month = start_date.month
    
    if current_month == 12:
        next_year = current_year + 1
        next_month = 1
    else:
        next_year = current_year
        next_month = current_month + 1
    
    next_15th = date(next_year, next_month, 15)
    month_name = MONTH_NAMES.get(next_month, "Unknown")
    
    return {
        "date": next_15th,
        "month_name": month_name,
        "year": next_year
    }

if __name__ == '__main__':
    result = get_next_15th()
    print(result["date"])
    print(f"The 15th of {result['month_name']} {result['year']}")