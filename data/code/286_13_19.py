def mm_to_inches(mm):
    return mm * 0.0393701

if __name__ == '__main__':
    sample_mm = 25
    inches_result = mm_to_inches(sample_mm)
    print(f"{sample_mm} mm is equal to {inches_result:.4f} inches")