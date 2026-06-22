CONVERSION_FACTOR = 0.3048

def convert_length(length):
    return length * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_length_ft = 25.0
    converted_length_m = convert_length(sample_length_ft)
    print(f"{sample_length_ft} ft converted to meters: {converted_length_m}")