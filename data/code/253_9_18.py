def find_the_middle_value_among_three_filter_valid(records):
    valid_records = []
    for record in records:
        if isinstance(record, tuple) and len(record) == 3 and all(isinstance(x, (int, float)) for x in record):
            valid_records.append(record)
    return valid_records

if __name__ == '__main__':
    sample_records = [
        (1, 2, 3),
        ('a', 'b', 'c'),
        (4.5, 6.7, 8.9),
        (10, 11),
        (12.0, 13.0, 14.0, 15.0)
    ]
    print(find_the_middle_value_among_three_filter_valid(sample_records))