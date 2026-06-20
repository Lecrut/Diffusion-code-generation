def compare_measurements(length1: float, length2: float) -> dict:
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return {"difference": difference, "ratio": ratio, "is_first_greater": is_greater}

if __name__ == "__main__":
    sample_length1 = 10.5
    sample_length2 = 4.2
    result = compare_measurements(sample_length1, sample_length2)
    print(result["difference"])
    print(result["ratio"])
    print(result["is_first_greater"])