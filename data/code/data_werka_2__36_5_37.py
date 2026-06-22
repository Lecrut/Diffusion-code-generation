def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("Function did not return a string")
        return result[::-1]
    return wrapper

class StringProcessor:
    def __init__(self, processing_func):
        self.processing_func = processing_func

    @reverse_string_decorator
    def process(self):
        return self.processing_func()

def sample_data_provider():
    return "Innovate with Alibaba Cloud"

if __name__ == '__main__':
    processor = StringProcessor(sample_data_provider)
    print(processor.process())