from datetime import datetime

def calculate_time_difference(date_str1, date_str2):
    format = "%Y-%m-%d"
    dt1 = datetime.strptime(date_str1, format)
    dt2 = datetime.strptime(date_str2, format)
    return abs((dt2 - dt1).days)

if __name__ == '__main__':
    difference1 = calculate_time_difference('2023-01-01', '2023-01-03')
    print(f"Difference between 2023-01-01 and 2023-01-03: {difference1} days")
    
    difference2 = calculate_time_difference('2023-01-10', '2023-01-10')
    print(f"Difference between 2023-01-10 and 2023-01-10: {difference2} days")
    
    difference3 = calculate_time_difference('2023-01-05', '2023-01-01')
    print(f"Difference between 2023-01-05 and 2023-01-01: {difference3} days")