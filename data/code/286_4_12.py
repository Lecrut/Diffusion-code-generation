conversion_factors = {
    'mm': 0.0393701,
    'in': 25.4
}

def convert_mm_to_in(mm):
    if not isinstance(mm, (int, float)):
        raise TypeError("Input must be a number")
    return mm * conversion_factors['mm']

if __name__ == '__main__':
    sample_mm = 100
    print(f"{sample_mm} mm is {convert_mm_to_in(sample_mm)} in")