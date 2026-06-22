conversion_factors = {
    'mm_to_in': 0.0393701,
}

def convert_mm_to_in(mm):
    return mm * conversion_factors['mm_to_in']

if __name__ == '__main__':
    sample_mm = 25
    result_in = convert_mm_to_in(sample_mm)
    print(result_in)