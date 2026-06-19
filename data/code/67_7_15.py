class NumberAdder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        try:
            num1 = float(self.a)
            num2 = float(self.b)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"10 + 5 = {adder1.add()}")
    
    adder2 = NumberAdder("hello", 3)
    print(f"'hello' + 3 = {adder2.add()}")
    
    adder3 = NumberAdder(2.5, 7.5)
    print(f"2.5 + 7.5 = {adder3.add()}")
    
    adder4 = NumberAdder(-10, 20)
    print(f"-10 + 20 = {adder4.add()}")
    
    adder5 = NumberAdder("a", "b")
    print(f"'a' + 'b' = {adder5.add()}")