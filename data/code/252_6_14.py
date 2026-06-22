def compare_two_simple_quantities_now_convert_all():
    sample_records = [
        ("apple", 5),
        ("banana", 3),
        ("orange", 2)
    ]
    
    converted_records = [(item[0], item[1] * 2) for item in sample_records]
    
    return converted_records

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_convert_all()
    print(result)