def find_the_middle_value_among_three_convert_all(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_records = [
        (10, 5, 20),
        (10, 5, 15),
        (10, 5, 15),
        (10, 5, 20)
    ]
    for record in sample_records:
        middle_value = find_the_middle_value_among_three_convert_all(*record)
        print(middle_value)