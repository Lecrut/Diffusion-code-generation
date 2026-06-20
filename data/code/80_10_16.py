import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        if date1 < date2:
            return date1
        elif date2 < date1:
            return date2
        else:
            return None
    except ValueError:
        return None

if __name__ == '__main__':
    date1_input = "2023-10-25"
    date2_input = "2023-10-15"
    result = compare_dates(date1_input, date2_input)
    print(result)