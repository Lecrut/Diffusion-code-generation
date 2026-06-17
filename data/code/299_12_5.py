class DateChecker:
    def is_weekend(self, date_input):
        try:
            import datetime
            date_obj = datetime.datetime.strptime(str(date_input), "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return weekday >= 5
        except ValueError:
            return False
if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = [
        "2023-10-28",                      
        "2023-10-29",                    
        "2023-10-30",          
        "2023-10-31",           
        "2023-11-05",                    
        "2023-11-06",          
        "2024-01-01"           
    ]
    for date_str in dates_to_check:
        result = checker.is_weekend(date_str)
        print(f"Date: {date_str}, Is Weekend: {result}")