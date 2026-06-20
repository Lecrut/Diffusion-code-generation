class Divider:
    def __init__(self):
        self.results = []

    def add_pair(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        result = num1 / num2
        self.results.append(result)

    def get_results(self):
        return self.results

if __name__ == '__main__':
    divider = Divider()
    divider.add_pair(4, 2)
    divider.add_pair(9, 3)
    divider.add_pair(10, 5)
    print(divider.get_results())