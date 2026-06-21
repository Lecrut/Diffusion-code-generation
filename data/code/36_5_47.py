def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("Function did not return a string")
        return result[::-1]
    return wrapper

class StringProcessor:
    def __init__(self, processor_func):
        self.processor_func = processor_func
    
    @reverse_string_decorator
    def process(self):
        return self.processor_func()

def sample_processor():
    return "Hello, Alibaba Cloud!"

if __name__ == '__main__':
    processor = StringProcessor(sample_processor)
    print(processor.process())