from datetime import datetime

def sort_dates(date_strings):
    if not isinstance(date_strings, list):
        raise TypeError("Input must be a list")
    if len(date_strings) == 0:
        return []
    validated_dates = []
    for item in date_strings:
        if not isinstance(item, str):
            raise TypeError("All items must be strings")
        parts = item.split('/')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {item}")
        try:
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])
        except ValueError:
            raise ValueError(f"Invalid date format: {item}")
        try:
            dt = datetime(year=year, month=month, day=day)
        except ValueError:
            raise ValueError(f"Invalid date format: {item}")
        validated_dates.append((dt, item))
    validated_dates.sort(key=lambda x: x[0])
    return [x[1] for x in validated_dates]

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)