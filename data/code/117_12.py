class NumberOperations:
    def find_difference(self, num1, num2):
        return abs(num1 - num2)
if __name__ == '__main__':
    operations = NumberOperations()
    num_a = 10
    num_b = 25
    difference = operations.find_difference(num_a, num_b)
    print(difference)