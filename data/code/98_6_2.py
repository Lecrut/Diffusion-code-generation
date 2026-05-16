import sys
def test_complex_scenario():
    str1 = "apple"
    str2 = "apple"
    str3 = "banana"
    num1 = 10
    num2 = 15
    threshold = 12
    condition1 = (str1 == str2)
    condition2 = (str3 != str1)
    condition3 = (num1 < num2)
    condition4 = (num2 > threshold)
    if condition1 and condition2 and condition3 and condition4:
        print("All conditions met.")
    else:
        print("One or more conditions failed.")
if __name__ == '__main__':
    test_complex_scenario()