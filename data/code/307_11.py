class Repeater:
    def repeat(self, callable_obj, num_iterations):
        for _ in range(num_iterations):
            callable_obj()
if __name__ == '__main__':
    repeater = Repeater()
    def increment():
        pass
    print("Testing with increment function:")
    repeater.repeat(increment, 3)
    def print_message():
        print("Hello")
    print("\nTesting with print_message function:")
    repeater.repeat(print_message, 2)