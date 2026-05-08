import argparse
import datetime
def get_day_of_week(date_string):
    try:
        date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.strftime('%A')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_string}. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a date string to the day of the week.")
    parser.add_argument("date", type=str, help="The date in YYYY-MM-DD format.")
    args = parser.parse_args(["2023-10-27"])
    try:
        day_name = get_day_of_week(args.date)
        print(day_name)
    except argparse.ArgumentTypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")