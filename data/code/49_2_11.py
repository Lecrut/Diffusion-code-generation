def compare_lengths(length1_str, length2_str):
    length1 = float(length1_str)
    length2 = float(length2_str)
    
    if length1 > length2:
        return f"The first length ({length1}) is longer than the second length ({length2})."
    elif length2 > length1:
        return f"The second length ({length2}) is longer than the first length ({length1})."
    else:
        return "Both lengths are equal."

if __name__ == '__main__':
    sample_length1 = "5.5"
    sample_length2 = "3.2"
    
    result = compare_lengths(sample_length1, sample_length2)
    print(result)