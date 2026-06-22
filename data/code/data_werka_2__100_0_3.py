def classify_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"

if __name__ == '__main__':
    print(classify_number(5))
    print(classify_number(-3))
    print(classify_number(0))