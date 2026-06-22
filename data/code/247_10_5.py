def sum_two_integers(a, b):
    return a + b

if __name__ == '__main__':
    sample_values = {3: 5, 7: 9}
    for num1, num2 in sample_values.items():
        result = sum_two_integers(num1, num2)
        print(f"Sum of {num1} and {num2} is {result}")