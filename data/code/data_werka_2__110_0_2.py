from datetime import datetime

def sort_dates_chronologically(date_strings):
    parsed_dates = [datetime.strptime(d, '%Y-%m-%d').date() for d in date_strings]
    paired = list(zip(parsed_dates, date_strings))
    paired.sort(key=lambda x: x[0])
    return [original for _, original in paired]

if __name__ == '__main__':
    sample_dates = ['2024-02-29', '2020-01-01', '2023-12-25', '2021-07-04', '2022-11-11']
    sorted_result = sort_dates_chronologically(sample_dates)
    print(sorted_result)