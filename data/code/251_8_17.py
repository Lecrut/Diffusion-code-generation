def determine_the_largest_number_present_compare():
    sample1 = 42
    sample2 = 99

    if sample1 > sample2:
        return {"largest": sample1, "comparison": f"{sample1} is greater than {sample2}"}
    elif sample1 < sample2:
        return {"largest": sample2, "comparison": f"{sample2} is greater than {sample1}"}
    else:
        return {"largest": sample1, "comparison": f"{sample1} and {sample2} are equal"}

if __name__ == '__main__':
    result = determine_the_largest_number_present_compare()
    print(result)