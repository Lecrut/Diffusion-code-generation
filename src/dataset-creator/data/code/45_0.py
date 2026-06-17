try:
    num1 = 5
    num2 = 3
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Inputs must be integers.")
    result = num1 + num2
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    print(result)
if __name__ == '__main__':
    pass