if __name__ == '__main__':
    num1 = 100
    num2 = 7
    
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    
    quotient = num1 // num2
    remainder = num1 % num2
    
    print(quotient)
    print(remainder)