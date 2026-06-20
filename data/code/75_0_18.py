from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    sample_date1 = "2023-01-01"
    sample_date2 = "2023-01-15"
    print(calculate_date_difference(sample_date1, sample_date2))