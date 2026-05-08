import datetime
def find_earliest_date(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        if date1 < date2:
            return date1
        else:
            return date2
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date_input1 = "2023-10-25"
    date_input2 = "2023-11-15"
    try:
        earliest = find_earliest_date(date_input1, date_input2)
        print(earliest.strftime('%Y-%m-%d'))
    except ValueError as e:
        print(f"Error: {e}")