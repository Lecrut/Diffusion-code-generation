def divide_numbers(dividend, divisor):
    division_map = {
        0: "Cannot divide by zero"
    }
    
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return division_map[0]

if __name__ == '__main__':
    result = divide_numbers(20.5, 4.2)
    print(result)