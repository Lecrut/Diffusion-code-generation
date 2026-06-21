class GCD:
    def calculate(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    gcd_instance = GCD()
    num1 = 48
    num2 = 18
    result = gcd_instance.calculate(num1, num2)
    print(f"GCD of {num1} and {num2} is: {result}")