def determine_positivity(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def test_determine_positivity():
    assert determine_positivity(10) == "Positive"
    assert determine_positivity(-5) == "Negative"
    assert determine_positivity(0) == "Zero"

if __name__ == '__main__':
    print(determine_positivity(10))
    print(determine_positivity(-5))
    print(determine_positivity(0))