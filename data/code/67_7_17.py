class NumberAdder:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        try:
            num1 = float(self.value1)
            num2 = float(self.value2)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"10 + 5 = {adder1.add()}")
    
    adder2 = NumberAdder("hello", 5)
    print(f"'hello' + 5 = {adder2.add()}")
    
    adder3 = NumberAdder(3.5, 2.1)
    print(f"3.5 + 2.1 = {adder3.add()}")
    
    adder4 = NumberAdder("a", "b")
    print(f"'a' + 'b' = {adder4.add()}")