def compare_floats(num1, num2):
    if abs(num1 - num2) < 1e-9:
        return "equal"
    elif num1 > num2:
        return "num1 greater"
    else:
        return "num2 greater"

if __name__ == '__main__':
    sample1 = (3.141592653589793, 3.141592653589793)
    print(compare_floats(*sample1))
    
    sample2 = (0.1 + 0.2, 0.3)
    print(compare_floats(*sample2))