from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    
    try:
        date_obj1 = datetime.strptime(date_str1, date_format)
        date_obj2 = datetime.strptime(date_str2, date_format)
        difference = abs((date_obj2 - date_obj1).days)
        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    print(calculate_date_difference("2023-01-01", "2023-01-15"))