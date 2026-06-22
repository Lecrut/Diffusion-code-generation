def determine_the_largest_number_present_compare():
    num1 = 42
    num2 = 73

    if num1 > num2:
        return {'largest': num1}
    elif num2 > num1:
        return {'largest': num2}
    else:
        return {'largest': 'equal'}

if __name__ == '__main__':
    result = determine_the_largest_number_present_compare()
    print(result)