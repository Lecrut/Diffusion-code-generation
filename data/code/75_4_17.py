import datetime

def calculate_days_difference(date1_str, date2_str):
    try:
        date_format = '%m/%d/%Y' if '/' in date1_str else '%Y-%m-%d'
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return "Error: Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD."

if __name__ == '__main__':
    result = calculate_days_difference("01/15/2023", "2024-03-20")
    print(result)