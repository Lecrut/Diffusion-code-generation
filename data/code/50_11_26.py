def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    return unique_to_set1 | unique_to_set2

if __name__ == '__main__':
    try:
        sample_set1 = {10, 20, 30, 40}
        sample_set2 = {30, 40, 50, 60}
        result_ab = symmetric_difference(sample_set1, sample_set2)
        print("Symmetric difference of sample_set1 and sample_set2:", result_ab)
        
        sample_set3 = {'apple', 'banana', 'cherry'}
        sample_set4 = {'banana', 'cherry', 'date'}
        result_cd = symmetric_difference(sample_set3, sample_set4)
        print("Symmetric difference of sample_set3 and sample_set4:", result_cd)
    except ValueError as e:
        print(e)