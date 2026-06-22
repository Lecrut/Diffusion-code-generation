def determine_the_largest_number_present_convert_all(records):
    return max(map(int, records))

if __name__ == '__main__':
    sample_records = ['3', '5', '2', '8', '1']
    print(determine_the_largest_number_present_convert_all(sample_records))