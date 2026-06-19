def calculate_symmetric_difference(set1, set2):
    return set1 ^ set2

if __name__ == '__main__':
    SAMPLE_SET_A = {10, 20, 30, 40}
    SAMPLE_SET_B = {30, 40, 50, 60}
    
    result = calculate_symmetric_difference(SAMPLE_SET_A, SAMPLE_SET_B)
    print("Symmetric difference between SAMPLE_SET_A and SAMPLE_SET_B:", result)