# Check if 'a' is different from 'b' using a one-line expression with sample values in main block
if __name__ == '__main__':
    a = 10
    b = 20
    result = (lambda x, y: x != y)(a, b)