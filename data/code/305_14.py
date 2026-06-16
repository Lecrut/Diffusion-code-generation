import sys
from datetime import datetime
def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            parsed_dates.append((date_obj, date_str))
        except ValueError:
            print(f"Error: Invalid date format for '{date_str}'. Expected YYYY-MM-DD.")
            sys.exit(1)
    parsed_dates.sort(key=lambda x: x[0])
    sorted_dates = [date_str for date_obj, date_str in parsed_dates]
    return sorted_dates
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2022-05-15",
        "2023-01-01",
        "2024-03-10",
        "invalid-date"
    ]
    print("Original dates provided:")
    for date in sample_dates:
        print(f"- {date}")
    try:
        sorted_list = sort_dates(sample_dates)
        print("\n--- Sorted Dates ---")
        for date in sorted_list:
            print(date)
    except SystemExit:
        print("\nSorting process aborted due to error.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")