import datetime
def sort_dates_from_file(filename):
    dates = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                date_str = line.strip()
                if date_str:
                    try:
                        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        dates.append(date_obj)
                    except ValueError:
                        print(f"Skipping invalid date format: {date_str}")
        dates.sort()
        return dates
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
if __name__ == '__main__':
    sample_filename = "dates.txt"
    with open(sample_filename, 'w') as f:
        f.write("2023-10-26\n")
        f.write("2023-01-01\n")
        f.write("2024-05-15\n")
        f.write("2023-12-31\n")
        f.write("invalid-date\n")
    sorted_dates = sort_dates_from_file(sample_filename)
    if sorted_dates:
        print("Sorted dates:")
        for dt in sorted_dates:
            print(dt.strftime('%Y-%m-%d'))