def determine_the_largest_number_present_compare():
    sample_value_1 = 42
    sample_value_2 = 99

    if sample_value_1 > sample_value_2:
        return {"largest": sample_value_1, "message": "Sample value 1 is larger"}
    elif sample_value_1 < sample_value_2:
        return {"largest": sample_value_2, "message": "Sample value 2 is larger"}
    else:
        return {"largest": sample_value_1, "message": "Both sample values are equal"}

if __name__ == '__main__':
    result = determine_the_largest_number_present_compare()
    print(result)