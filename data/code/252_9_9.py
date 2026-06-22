def compare_two_simple_quantities_now_filter_valid(sample_records):
    valid_records = []
    for record in sample_records:
        if 'quantity1' in record and 'quantity2' in record:
            try:
                quantity1 = float(record['quantity1'])
                quantity2 = float(record['quantity2'])
                if quantity1 >= 0 and quantity2 >= 0:
                    valid_records.append((quantity1, quantity2))
            except ValueError:
                continue
    return valid_records

if __name__ == '__main__':
    sample_values = [
        {'quantity1': '3.5', 'quantity2': '4.2'},
        {'quantity1': '-1.0', 'quantity2': '2.0'},
        {'quantity1': '5.0', 'quantity2': 'abc'},
        {'quantity1': '7.8', 'quantity2': '9.1'}
    ]
    valid_values = compare_two_simple_quantities_now_filter_valid(sample_values)
    print(valid_values)