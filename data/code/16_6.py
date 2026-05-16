def determine_positivity(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
if __name__ == '__main__':
    assert determine_positivity(5) == "positive"
    assert determine_positivity(-3) == "negative"
    assert determine_positivity(0) == "zero"
    assert determine_positivity(100) == "positive"
    assert determine_positivity(-0.001) == "negative"
    assert determine_positivity(0.0) == "zero"
    print("All tests passed.")