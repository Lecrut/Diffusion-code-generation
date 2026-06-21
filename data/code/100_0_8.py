def determine_sign(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"

if __name__ == '__main__':
    test_values = [15, -20, 0]
    for val in test_values:
        print(determine_sign(val))