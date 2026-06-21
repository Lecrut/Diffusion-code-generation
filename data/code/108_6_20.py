from datetime import date

def get_days_for_dates(date_strings):
    results = []
    for ds in date_strings:
        parts = ds.split("-")
        y = int(parts[0])
        m = int(parts[1])
        d = int(parts[2])
        dt = date(y, m, d)
        results.append(dt.day)
    return results

if __name__ == '__main__':
    sample_dates = ["2023-01-15", "2024-02-29", "2025-12-31"]
    days = get_days_for_dates(sample_dates)
    print(days)