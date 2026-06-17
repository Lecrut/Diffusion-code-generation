from datetime import date
def get_day_of_week(year: int, month: int, day: int) -> str:
    try:
        d = date(year, month, day)
        return d.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {year}-{month}-{day}") from e
if __name__ == '__main__':
    test_cases = [
        (2023, 1, 5),              
        (2024, 6, 18) ,          
        (2020, 7, 9) ,         
        (2022, 12, 25)        
    ]
    print("Input Year-Month-Day -> Output Day of Week")
    for y, m, d in test_cases:
        result = get_day_of_week(y, m, d)
        formatted_date = f"{y}-{m:02d}-{d:02d}"
        print(f"Date: {formatted_date} => {result}")