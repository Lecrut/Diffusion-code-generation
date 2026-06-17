class Repeater:
    def repeat(self, callable_obj, num_iterations):
        for _ in range(num_iterations):
            callable_obj()
if __name__ == '__main__':
    repeater = Repeater()
    def sample_function():
        pass
    print("Testing Repeater...")
    repeater.repeat(sample_function, 5)
    def another_sample_function():
        print("Executed")
    print("\nTesting another function...")
    repeater.repeat(another_sample_function, 3)