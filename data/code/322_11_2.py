def divide_quantities(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except TypeError:
        return "Error: Both inputs must be numeric."
    except ZeroDivisionError:
        return "Error: Denominator cannot be zero."
if __name__ == '__main__':
    print(divide_quantities(10.0, 2.5))
    print(divide_quantities(15.0, 3.0))
    print(divide_quantities(10.0, 0.0))
    print(divide_quantities("a", 2.0))
    print(divide_quantities(5.0, "b"))