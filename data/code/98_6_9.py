def test_complex_scenario():
    string1 = "hello"
    string2 = "world"
    number1 = 42
    number2 = 24

    if string1 == "hello" and string2 != "hello" and number1 > number2:
        return "All conditions met"
    else:
        return "Conditions not met"

if __name__ == '__main__':
    print(test_complex_scenario())