# Check if variable 'a' is different from variable 'b' using a concise one-line expression
result = (lambda: a != b)()  # This line evaluates to True or False based on whether a and b are unequal

if __name__ == '__main__':
    a = 10
    b = 20
    print(result)  # Expected output: True
    
    c = 5
    d = 5
    result_cd = (lambda x, y: x != y)(c, d)
    print(result_cd)  # Expected output: False