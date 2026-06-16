def check_precedence(date_a: str, date_b: str) -> bool:
    format_str = '%m/%d/%Y'
    try:
        date_a_obj = datetime.datetime.strptime(date_a, format_str)
        date_b_obj = datetime.datetime.strptime(date_b, format_str)
        return date_a_obj < date_b_obj
    except ValueError:
        raise ValueError("Invalid date format provided. Expected 'MM/DD/YYYY'.")
if __name__ == '__main__':
    import datetime
    date1 = "01/15/2023"
    date2 = "03/20/2023"
    date3 = "12/31/2022"
    date4 = "01/15/2023"
    print(f"Is {date1} before {date2}? {check_precedence(date1, date2)}")
    print(f"Is {date2} before {date1}? {check_precedence(date2, date1)}")
    print(f"Is {date3} before {date1}? {check_precedence(date3, date1)}")
    print(f"Is {date4} before {date4}? {check_precedence(date4, date4)}")