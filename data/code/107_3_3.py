class DateFormatter:
    def format_date(self, date_string):
        try:
            if not isinstance(date_string, str):
                raise ValueError("Input must be a string")
            parts = date_string.split('-')
            if len(parts) != 3:
                raise ValueError("Date format incorrect. Expected YYYY-MM-DD")
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid month or day values")
            formatted_date = f"{year}{month:02d}{day:02d}"
            return int(formatted_date)
        except ValueError as e:
            raise ValueError(f"Error processing date string '{date_string}': {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    formatter = DateFormatter()
    sample_dates = [
        "2023-10-27",
        "1999-01-01",
        "2024-02-29",
        "2023/10/27",                       
        "2023-13-01",                      
        "2023-02-30",                    
        "not-a-date"                         
    ]
    for date_str in sample_dates:
        try:
            result = formatter.format_date(date_str)
            print(f"Input: {date_str} -> Output: {result}")
        except ValueError as e:
            print(f"Input: {date_str} -> Error: {e}")
        except Exception as e:
            print(f"Input: {date_str} -> Unexpected Error: {e}")