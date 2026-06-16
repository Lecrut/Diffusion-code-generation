class Repeater:
    def repeat(self, callable_obj, num_iterations):
        for _ in range(num_iterations):
            callable_obj()
if __name__ == '__main__':
    repeater = Repeater()
    def incrementer():
        pass
    print("Testing with incrementer:")
    repeater.repeat(incrementer, 5)
    def adder(a, b):
        return a + b
    print("\nTesting with adder (using lambda for argument passing):")
    def multiply_by_two():
        pass
    print("Testing with multiply_by_two:")
    repeater.repeat(multiply_by_two, 3)