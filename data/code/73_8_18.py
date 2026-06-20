from datetime import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        date_obj1 = datetime.strptime(date_str1, date_format)
        date_obj2 = datetime.strptime(date_str2, date_format)
        
        time_diff = abs((date_obj2 - date_obj1).total_seconds())
        return time_diff
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD HH:MM:SS."

if __name__ == '__main__':
    sample_date1 = "2023-10-05 14:30:00"
    sample_date2 = "2023-10-06 15:45:00"
    
    result = calculate_time_difference(sample_date1, sample_date2)
    print(result)