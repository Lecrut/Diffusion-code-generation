class NumberAdder:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def calculate_sum(self):
        try:
            num1 = float(self.attr1)
            num2 = float(self.attr2)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    adder1 = NumberAdder(10, 5)
    print(f"10 + 5 = {adder1.calculate_sum()}")
    
    adder2 = NumberAdder("hello", 3)
    print(f"'hello' + 3 = {adder2.calculate_sum()}")
    
    adder3 = NumberAdder(2.5, 7.5)
    print(f"2.5 + 7.5 = {adder3.calculate_sum()}")
    
    adder4 = NumberAdder(-10, 20)
    print(f"-10 + 20 = {adder4.calculate_sum()}")
    
    adder5 = NumberAdder("a", "b")
    print(f"'a' + 'b' = {adder5.calculate_sum()}")