def sort_date_strings(date_list):
    date_objects = [d.split('-') for d in date_list]
    date_tuples = [(int(parts[0]), int(parts[1]), int(parts[2])) for parts in date_objects]
    paired = list(zip(date_tuples, date_list))
    paired.sort(key=lambda item: item[0])
    return [original for _, original in paired]

if __name__ == '__main__':
    raw_dates = ['1999-12-31', '2000-01-01', '1995-06-15', '2000-02-29', '1999-12-31']
    sorted_dates = sort_date_strings(raw_dates)
    print(sorted_dates)