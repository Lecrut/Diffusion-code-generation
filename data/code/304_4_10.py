from datetime import datetime
def check_precedence(date_a: str, date_b: str) -> bool:
    format_str = '%m/%d/%Y'
    try:
        date_a_obj = datetime.strptime(date_a, format_str)
        date_b_obj = datetime.strptime(date_b, format_str)
        return date_a_obj < date_b_obj
    except ValueError:
        raise ValueError("Invalid date format provided. Expected 'MM/DD/YYYY'.")
if __name__ == '__main__':
    date1 = "01/15/2023"
    date2 = "03/20/2023"
    print(f"Is {date1} before {date2}? {check_precedence(date1, date2)}")
    date3 = "12/31/2022"
    date4 = "01/01/2023"
    print(f"Is {date3} before {date4}? {check_precedence(date3, date4)}")
    date5 = "05/10/2023"
    date6 = "05/10/2023"
    print(f"Is {date5} before {date6}? {check_precedence(date5, date6)}")
    date7 = "01/01/2024"
    date8 = "12/31/2023"
    print(f"Is {date7} before {date8}? {check_precedence(date7, date8)}")