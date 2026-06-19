def compare_lengths(len1, len2):
    result = (
        'len1 is greater' if len1 > len2 else
        'len2 is smaller' if len1 < len2 else
        'equal'
    )
    return result

if __name__ == '__main__':
    SAMPLE_LENGTH_1 = 30
    SAMPLE_LENGTH_2 = 45
    print(f"Comparing {SAMPLE_LENGTH_1} and {SAMPLE_LENGTH_2}: {compare_lengths(SAMPLE_LENGTH_1, SAMPLE_LENGTH_2)}")
    
    SAMPLE_LENGTH_3 = 75
    SAMPLE_LENGTH_4 = 75
    print(f"Comparing {SAMPLE_LENGTH_3} and {SAMPLE_LENGTH_4}: {compare_lengths(SAMPLE_LENGTH_3, SAMPLE_LENGTH_4)}")
    
    SAMPLE_LENGTH_5 = 20
    SAMPLE_LENGTH_6 = 10
    print(f"Comparing {SAMPLE_LENGTH_5} and {SAMPLE_LENGTH_6}: {compare_lengths(SAMPLE_LENGTH_5, SAMPLE_LENGTH_6)}")