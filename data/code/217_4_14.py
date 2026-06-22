RELATIONSHIP_FORMAT = '{} {} {}'

def compare_numbers(a, b):
    return RELATIONSHIP_FORMAT.format(a, '>' if a > b else '<' if a < b else '==', b)

if __name__ == '__main__':
    num1 = 42
    num2 = 17
    print(compare_numbers(num1, num2))