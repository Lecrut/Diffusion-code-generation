def determine_the_largest_number_present_convert_all(records):
    return max(int(record) for record in records)

if __name__ == '__main__':
    sample_records = ['34', '56', '12', '89', '7']
    print(determine_the_largest_number_present_convert_all(sample_records))