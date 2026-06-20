class NumberComparer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_larger_number(self):
        if self.num1 > self.num2:
            return self.num1
        elif self.num2 > self.num1:
            return self.num2
        else:
            return None

if __name__ == '__main__':
    comparer = NumberComparer(100, 200)
    larger_number = comparer.get_larger_number()
    if larger_number is not None:
        print(f"The larger number is: {larger_number}")
    else:
        print("The numbers are equal")