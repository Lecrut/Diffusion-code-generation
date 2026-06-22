from datetime import datetime

MONTH_MAP = {
    '01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6,
    '07': 7, '08': 8, '09': 9, '10': 10, '11': 11, '12': 12
}

def sort_dates_chronologically(date_strings):
    result = []
    for ds in date_strings:
        parts = ds.split('/')
        day = int(parts[0])
        month_str = parts[1]
        year = int(parts[2])
        if month_str not in MONTH_MAP:
            raise ValueError(f"Invalid month: {month_str}")
        month = MONTH_MAP[month_str]
        dt = datetime(year=year, month=month, day=day)
        result.append((dt, ds))
    result.sort(key=lambda pair: pair[0])
    return [pair[1] for pair in result]

if __name__ == '__main__':
    samples = ['31/12/2023', '01/01/2023', '15/02/2023', '28/02/2023']
    sorted_list = sort_dates_chronologically(samples)
    print(sorted_list)