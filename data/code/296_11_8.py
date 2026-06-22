def calculate_ratio(num1, den1, num2, den2):
    try:
        ratio1 = num1 / den1
        ratio2 = num2 / den2
        result = ratio1 / ratio2
        return f'{num1}:{den1} / {num2}:{den2} = {result}'
    except ZeroDivisionError:
        return 'Denominator cannot be zero'
    except TypeError as e:
        return str(e)
if __name__ == '__main__':
    print(calculate_ratio(6, 9, 3, 4))
    print(calculate_ratio(10, 15, 2, 5))
    print(calculate_ratio(7, 0, 2, 5))