DECIMAL_PLACES = 4

def calculate_difference(num1, num2):
    return round(num1 - num2, DECIMAL_PLACES)

if __name__ == '__main__':
    NUM1 = 15.3456789
    NUM2 = 7.1234567
    difference = calculate_difference(NUM1, NUM2)
    print(difference)