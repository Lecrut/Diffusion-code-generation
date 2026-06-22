def determine_the_largest_number_present_convert_all(records):
    largest_numbers = []
    for record in records:
        numbers = list(map(int, record.split()))
        largest_numbers.append(max(numbers))
    return largest_numbers
if __name__ == '__main__':
    sample_records = ['1 2 3', '4 5 6 7', '8 9']
    result = determine_the_largest_number_present_convert_all(sample_records)
    print(result)