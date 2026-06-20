def test_complex_scenario():
    str1 = "hello"
    str2 = "world"
    num1 = 10
    num2 = 20

    if str1 == "hello" and str2 != "hello" and num1 < num2:
        return "All conditions met"
    else:
        return "Conditions not met"

if __name__ == '__main__':
    print(test_complex_scenario())