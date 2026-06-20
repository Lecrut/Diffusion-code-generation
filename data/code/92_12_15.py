def opposite_truth_value(value):
    if value.lower() == 'true':
        return 'False'
    elif value.lower() == 'false':
        return 'True'
    else:
        raise ValueError("Input must be a string representation of a boolean ('True' or 'False')")

if __name__ == '__main__':
    sample1 = 'True'
    print(f"Opposite of {sample1}: {opposite_truth_value(sample1)}")
    
    sample2 = 'false'
    print(f"Opposite of {sample2}: {opposite_truth_value(sample2)}")