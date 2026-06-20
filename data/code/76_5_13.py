import datetime

def validate_date_format(date_str):
    date_format = '%m/%d/%Y'
    try:
        datetime.datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

def calculate_date_difference(date_str1, date_str2):
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")
    date1 = datetime.datetime.strptime(date_str1, '%m/%d/%Y')
    date2 = datetime.datetime.strptime(date_str2, '%m/%d/%Y')
    difference = abs((date1 - date2).days)
    return difference

if __name__ == '__main__':
    date_a = '01/15/2023'
    date_b = '03/20/2023'
    print(f"Difference between {date_a} and {date_b}: {calculate_date_difference(date_a, date_b)} days")
    date_c = '12/31/2022'
    date_d = '01/01/2023'
    print(f"Difference between {date_c} and {date_d}: {calculate_date_difference(date_c, date_d)} days")
    date_e = '10/10/2023'
    print(f"Difference between {date_a} and {date_e}: {calculate_date_difference(date_a, date_e)} days")