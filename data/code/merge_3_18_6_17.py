# Check if 'a' is greater than 'b' using a comparison operator in one line
result = (lambda: a > b)()  # This evaluates to True or False based on values of a and b

if __name__ == '__main__':
    a, b = 10, 5
    print(result)