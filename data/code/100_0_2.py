NUMERIC_CLASSES = {
    1: "positive",
    -1: "negative",
    0: "zero",
}

def categorize_number(value):
    if value > 0:
        sign = 1
    elif value < 0:
        sign = -1
    else:
        sign = 0
    return NUMERIC_CLASSES[sign]

if __name__ == '__main__':
    print(categorize_number(42))
    print(categorize_number(-9))
    print(categorize_number(0))