import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = '%m/%d/%Y'
    return abs((datetime.datetime.strptime(date_str2, date_format) - datetime.datetime.strptime(date_str1, date_format)).days)

if __name__ == '__main__':
    print(f"Difference between 01/15/2023 and 03/20/2023: {calculate_date_difference('01/15/2023', '03/20/2023')} days")
    print(f"Difference between 12/31/2022 and 01/01/2023: {calculate_date_difference('12/31/2022', '01/01/2023')} days")