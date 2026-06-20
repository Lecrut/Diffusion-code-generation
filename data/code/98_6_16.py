def check_conditions():
    str1 = "apple"
    str2 = "banana"
    num1 = 5
    num2 = 10
    condition1 = (str1 == str1)
    condition2 = (str1 != str2)
    condition3 = (num1 < num2)
    if condition1 and condition2 and condition3:
        return "All conditions met."
    else:
        return "One or more conditions failed."

if __name__ == '__main__':
    result = check_conditions()
    print(result)