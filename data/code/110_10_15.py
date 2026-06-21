from datetime import datetime

def sort_date_strings(date_strings):
    if not date_strings:
        return []
    parsed = [datetime.strptime(d, '%Y-%m-%d') for d in date_strings]
    combined = list(zip(parsed, date_strings))
    combined.sort(key=lambda x: x[0])
    return [entry[1] for entry in combined]

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    result = sort_date_strings(sample_dates)
    print(result)