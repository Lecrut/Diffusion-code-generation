from datetime import datetime

def sort_dates(date_strings):
    if not isinstance(date_strings, list):
        raise ValueError("Input must be a list")
    if len(date_strings) == 0:
        return []
    
    date_map = {
        'year': 0,
        'month': 1,
        'day': 2
    }
    
    def parse_to_tuple(date_str):
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        return (y, m, d)
    
    sorted_dates = sorted(date_strings, key=lambda x: parse_to_tuple(x))
    return sorted_dates

if __name__ == '__main__':
    raw_dates = ['2024-01-15', '2020-12-01', '2021-02-30', '2023-05-20']
    result = sort_dates(raw_dates)
    print(result)