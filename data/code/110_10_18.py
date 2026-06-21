from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def sort_dates(date_strings):
    if not date_strings:
        return []
    date_objects = []
    for d in date_strings:
        parsed = datetime.strptime(d, DATE_FORMAT)
        date_objects.append((parsed, d))
    date_objects.sort(key=lambda pair: pair[0])
    return [pair[1] for pair in date_objects]

if __name__ == '__main__':
    input_dates = ['2024-02-29', '2020-02-29', '2023-02-28', '2021-02-28']
    sorted_result = sort_dates(input_dates)
    print(sorted_result)