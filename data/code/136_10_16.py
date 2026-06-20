class LogicalOperatorsDemo:
    def __init__(self):
        self.a = True
        self.b = False

    def evaluate_and(self):
        return self.a and self.b

    def evaluate_or(self):
        return self.a or self.b

    def evaluate_not_a(self):
        return not self.a

def main():
    demo = LogicalOperatorsDemo()
    print("--- Logical Operators Demonstration ---")
    print(f"a = {demo.a}, b = {demo.b}")
    and_result = demo.evaluate_and()
    or_result = demo.evaluate_or()
    not_a_result = demo.evaluate_not_a()
    print("\n--- Results ---")
    print(f"a AND b: {and_result}")
    print(f"a OR b: {or_result}")
    print(f"NOT a: {not_a_result}")

if __name__ == '__main__':
    main()