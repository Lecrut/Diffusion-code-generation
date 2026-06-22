def compare_two_simple_quantities_now_convert_all():
    sample_records = [
        {"quantity1": 10, "quantity2": 5},
        {"quantity1": 3, "quantity2": 7},
        {"quantity1": 8, "quantity2": 8}
    ]
    converted_records = []
    for record in sample_records:
        converted_record = {
            "quantity1": record["quantity1"] * 2,
            "quantity2": record["quantity2"] + 3
        }
        converted_records.append(converted_record)
    return converted_records

if __name__ == '__main__':
    print(compare_two_simple_quantities_now_convert_all())