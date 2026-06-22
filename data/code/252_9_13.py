def compare_two_simple_quantities_now_filter_valid(sample_records):
    valid_records = []
    for record in sample_records:
        if record['quantity'] > 0 and record['unit'].isalpha():
            valid_records.append(record)
    return valid_records

if __name__ == '__main__':
    sample_values = [
        {'quantity': 10, 'unit': 'kg'},
        {'quantity': -5, 'unit': 'kg'},
        {'quantity': 20, 'unit': 'g'},
        {'quantity': 30, 'unit': ''},
        {'quantity': 40, 'unit': 'm'}
    ]
    print(compare_two_simple_quantities_now_filter_valid(sample_values))