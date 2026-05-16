import sys
def run_test():
    str1 = "apple"
    str2 = "apple"
    str3 = "banana"
    num1 = 10
    num2 = 10
    num3 = 5
    condition1 = (str1 == str2)
    condition2 = (str1 != str3)
    condition3 = (num1 > num3)
    if condition1 and condition2 and condition3:
        print("All conditions met.")
    else:
        print("Conditions not fully met.")
if __name__ == '__main__':
    run_test()