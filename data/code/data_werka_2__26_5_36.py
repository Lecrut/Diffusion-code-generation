def check_first_arg_greater_than_100(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 100:
            raise ValueError("The first argument must be greater than 100")
        return func(*args, **kwargs)
    return wrapper

class SampleClass:
    @check_first_arg_greater_than_100
    def add_numbers(self, a, b):
        return a + b

    @check_first_arg_greater_than_100
    def multiply_numbers(self, a, b):
        return a * b

if __name__ == '__main__':
    try:
        sample = SampleClass()
        result_add = sample.add_numbers(150, 200)
        print("Addition Result:", result_add)
        
        result_multiply = sample.multiply_numbers(150, 50)
        print("Multiplication Result:", result_multiply)
    except ValueError as e:
        print(e)