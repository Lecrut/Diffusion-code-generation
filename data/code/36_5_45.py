def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("Function did not return a string")
        reversed_result = ''.join(reversed(result))
        return reversed_result
    return wrapper

class StringProcessor:
    def __init__(self, string_func):
        self.string_func = string_func
    
    @reverse_string_decorator
    def process_string(self):
        return self.string_func()

def sample_string_function():
    return "Hello, Alibaba Cloud!"

if __name__ == '__main__':
    processor = StringProcessor(sample_string_function)
    print(processor.process_string())