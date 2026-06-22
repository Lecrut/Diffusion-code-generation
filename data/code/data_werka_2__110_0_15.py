def sort_date_strings(date_list):
    if not date_list:
        return []
    year_index = 0
    month_index = 5
    day_index = 8
    formatted_dates = [
        (
            int(d[year_index:year_index + 4]),
            int(d[month_index:month_index + 2]),
            int(d[day_index:day_index + 2])
        )
        for d in date_list
    ]
    paired_dates = list(zip(formatted_dates, date_list))
    paired_dates.sort(key=lambda pair: pair[0])
    return [original for _, original in paired_dates]

if __name__ == '__main__':
    sample_dates = ['2024-05-10', '2020-01-01', '2023-12-31', '2021-07-04', '2022-11-11']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)