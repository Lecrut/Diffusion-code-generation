class Repeater:
    def repeat(self, callable_obj, num_iterations):
        for _ in range(num_iterations):
            callable_obj()
if __name__ == '__main__':
    repeater = Repeater()
    def increment():
        pass
    print("Testing repeater...")
    repeater.repeat(increment, 3)
    def print_message():
        print("Executed")
    print("\nTesting with printing function...")
    repeater.repeat(print_message, 2)