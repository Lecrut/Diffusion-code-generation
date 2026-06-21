def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("Function did not return a string")
        return result[::-1]
    return wrapper

class StringProcessor:
    def __init__(self, value):
        self.value = value
    
    @reverse_string_decorator
    def get_reversed(self):
        return self.value

if __name__ == '__main__':
    processor = StringProcessor("Hello, Alibaba Cloud!")
    print(processor.get_reversed())