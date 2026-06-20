class Divider:
    def divide(self, x, y):
        return x / y if y != 0 else 'Division by zero'

if __name__ == '__main__':
    divider = Divider()
    print(divider.divide(150.75, 3.0))