import sys
from datetime import datetime
def sort_dates(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    if date1 < date2:
        return date1, date2
    else:
        return date2, date1
if __name__ == '__main__':
    date1_input = "2023-10-26"
    date2_input = "2023-10-01"
    try:
        date1_str = date1_input
        date2_str = date2_input
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 < date2:
            ordered_date1 = date1
            ordered_date2 = date2
        else:
            ordered_date1 = date2
            ordered_date2 = date1
        print(f"Chronologically ordered pair: ({ordered_date1.strftime('%Y-%m-%d')}, {ordered_date2.strftime('%Y-%m-%d')})")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)