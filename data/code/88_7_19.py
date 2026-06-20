def verify_booleans(boolean_one: bool, boolean_two: bool) -> str:
    if boolean_one and boolean_two:
        return "Both booleans are True"
    else:
        return "At least one boolean is False"

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = verify_booleans(sample1, sample2)
    print(result)