def mm_to_inches(mm):
    conversion_factor = 0.0393701
    inches = mm * conversion_factor
    return inches

if __name__ == '__main__':
    sample_mm = 25
    result_inches = mm_to_inches(sample_mm)
    print(f"{sample_mm} millimeters is equal to {result_inches:.4f} inches")
    
    another_sample_mm = 100
    another_result_inches = mm_to_inches(another_sample_mm)
    print(f"{another_sample_mm} millimeters is equal to {another_result_inches:.4f} inches")