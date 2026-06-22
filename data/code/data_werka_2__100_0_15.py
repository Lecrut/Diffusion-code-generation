def determine_sign(number):
    if number > 0:
        label = "positive"
    elif number < 0:
        label = "negative"
    else:
        label = "zero"
    return label

if __name__ == '__main__':
    test_values = [15, -20, 0]
    for val in test_values:
        print(determine_sign(val))