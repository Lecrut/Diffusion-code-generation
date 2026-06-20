def extract_digits(input_string):
    result = []
    for char in input_string:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = "User123@domain.com, Phone: 555-0199"
    extracted_value = extract_digits(sample_data)
    print(extracted_value)
    
    sample_data_two = "No numbers here!"
    extracted_value_two = extract_digits(sample_data_two)
    print(extracted_value_two)
    
    sample_data_three = "9876543210"
    extracted_value_three = extract_digits(sample_data_three)
    print(extracted_value_three)