def test_conditional_expressions():
    value = 75
    if value >= 90:
        result = "Grade A"
    elif value >= 80:
        result = "Grade B"
    elif value >= 70:
        result = "Grade C"
    else:
        result = "Grade F"
    print(f"Input Value: {value}")
    print(f"Result: {result}")
if __name__ == '__main__':
    test_conditional_expressions()