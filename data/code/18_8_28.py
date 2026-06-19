class Number:
    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if not isinstance(other, Number):
            raise ValueError("Argument must be an instance of Number")
        
        if self.value > other.value:
            return "greater than"
        elif self.value < other.value:
            return "less than"
        else:
            return "equal to"

if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(20)
    result = num1.compare(num2)
    print(f"Number 1 is {result} Number 2")