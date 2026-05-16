class NumberOperations:
    def find_difference(self, num1, num2):
        return abs(num1 - num2)
if __name__ == '__main__':
    operations = NumberOperations()
    number1 = 10
    number2 = 25
    difference = operations.find_difference(number1, number2)
    print(difference)