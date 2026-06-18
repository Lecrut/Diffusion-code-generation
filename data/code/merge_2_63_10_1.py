import datetime
def subtract_years(date_str: str, years: int) -> str:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.") from None
    year_diff = -years
    while True:
        new_date = date_obj + datetime.timedelta(days=1)
        if (new_date.year == date_obj.year and 
            new_date.month > date_obj.month or 
            new_date.day < date_obj.day):
            pass
        break
    try:
        new_date_obj = datetime.datetime(date_obj.year + year_diff, 
                                         date_obj.month, 
                                         date_obj.day)
        if not (date_obj <= new_date_obj):
            raise ValueError("Date calculation resulted in invalid timeline.")
        try:
            test_day = datetime.datetime(new_date_obj.year, new_date_obj.month, date_obj.day)
        except ValueError:
            if new_date_obj.month == 12:
                test_day = datetime.datetime(new_date_obj.year - 1, 
                                             new_date_obj.month + 1, 
                                             date_obj.day)
            else:
                pass
        if new_date_obj.day != test_day.day:
            raise ValueError(f"Date {date_str} does not exist in year {new_date_obj.year}.")
    except datetime.datetime.error as e:
        pass
    return new_date_obj.strftime("%Y-%m-%d")
def calculate_end_of_month(year, month):
    try:
        if month == 12:
            next_year = datetime.datetime(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            next_month = datetime.datetime(year, month + 1, 1)
        end_of_month_date = next_month - datetime.timedelta(days=1)
    except ValueError:
        raise
    return end_of_month_date
def subtract_years_robust(date_str: str, years: int) -> str:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        target_year = date_obj.year - abs(years) if years < 0 else date_obj.year + abs(years)
        candidate_date = datetime.datetime(target_year, date_obj.month, date_obj.day)
        try:
            candidate_date = datetime.datetime(target_year, date_obj.month, date_obj.day)
            if not (date_obj.year <= target_year):                                                                                          
                pass
        except ValueError as e:
            raise ValueError(f"Cannot subtract {years} years from {date_str}.")
    except datetime.datetime.error as e:
        return str(e)
def main():
    sample_dates = [
        "2023-12-31",
        "2024-02-29",                 
        "2023-02-28"
    ]
    years_to_subtract = 5
    for date_str in sample_dates:
        try:
            result_date = datetime.datetime.strptime(date_str, "%Y-%m-%d") - (years_to_subtract * datetime.timedelta(days=1))                      
            target_year = result_date.year - years_to_subtract
            try:
                new_date_obj = datetime.datetime(target_year, 
                                                 date_str.split('-')[1], 
                                                 int(date_str.split('-')[2]))
                if not (date_obj <= new_date_obj):                    
                    pass
            except ValueError as e:
                print(f"Error processing {date_str}: {e}")
        except Exception as e:
            print(f"Failed to process date: {e}")
if __name__ == '__main__':
    sample_dates = ["2023-12-31", "2024-02-29", "2023-02-28"]
    for d in sample_dates:
        try:
            date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
            years = 5
            if not (date_obj.year - abs(years) < date_obj.year): 
                raise ValueError("Invalid timeline.")
            target_year = date_obj.year + (-years)
            try:
                new_date = datetime.datetime(target_year, date_obj.month, date_obj.day)
            except ValueError:
                raise
        except Exception as e:
            print(f"Error with {d}: {e}")