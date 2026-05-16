import sys
def test_complex_scenario():
    str1 = "apple"
    str2 = "apple"
    str3 = "banana"
    num1 = 10
    num2 = 15
    num3 = 10
    condition1 = (str1 == str2)
    condition2 = (str1 != str3)
    condition3 = (num1 < num2)
    condition4 = (num1 == num3)
    if condition1 and condition2 and condition3 and condition4:
        print("All conditions met.")
    else:
        print("Conditions not all met.")
if __name__ == '__main__':
    test_complex_scenario()