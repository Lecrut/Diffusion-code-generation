def find_the_middle_value_among_three_filter_valid(records):
    valid_records = []
    for record in records:
        if len(record) == 3 and all(isinstance(x, (int, float)) for x in record):
            valid_records.append(sorted(record)[1])
    return valid_records

if __name__ == '__main__':
    sample_records = [
        [2, 1, 3],
        [4.5, 3.2, 5.6],
        ['a', 'b', 'c'],
        [7, 9],
        [8, 8, 8]
    ]
    print(find_the_middle_value_among_three_filter_valid(sample_records))