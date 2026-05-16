from datetime import date
class DateChecker:
    def is_weekday(self, date_obj: date) -> bool:
        weekday = date_obj.weekday()
        return 0 <= weekday <= 4
if __name__ == '__main__':
    checker = DateChecker()
    date1 = date(2023, 10, 2)          
    date2 = date(2023, 10, 3)           
    date3 = date(2023, 10, 4)             
    date4 = date(2023, 10, 5)            
    date5 = date(2023, 10, 6)          
    date6 = date(2023, 10, 7)            
    date7 = date(2023, 10, 8)          
    print(f"Is {date1} a weekday? {checker.is_weekday(date1)}")
    print(f"Is {date2} a weekday? {checker.is_weekday(date2)}")
    print(f"Is {date3} a weekday? {checker.is_weekday(date3)}")
    print(f"Is {date4} a weekday? {checker.is_weekday(date4)}")
    print(f"Is {date5} a weekday? {checker.is_weekday(date5)}")
    print(f"Is {date6} a weekday? {checker.is_weekday(date6)}")
    print(f"Is {date7} a weekday? {checker.is_weekday(date7)}")