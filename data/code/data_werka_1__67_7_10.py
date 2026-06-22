class NumberAdder:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def add_attributes(self):
        try:
            num1 = float(self.attr1)
            num2 = float(self.attr2)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"10 + 5 = {adder1.add_attributes()}")
    
    adder2 = NumberAdder("hello", 5)
    print(f"'hello' + 5 = {adder2.add_attributes()}")
    
    adder3 = NumberAdder(3.5, 2.1)
    print(f"3.5 + 2.1 = {adder3.add_attributes()}")
    
    adder4 = NumberAdder("a", "b")
    print(f"'a' + 'b' = {adder4.add_attributes()}")