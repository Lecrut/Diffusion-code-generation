conversion_factors = {
    'mm': 0.0393701,
}

def millimeters_to_inches(mm):
    return mm * conversion_factors['mm']

if __name__ == '__main__':
    sample_mm = 25
    print(millimeters_to_inches(sample_mm))