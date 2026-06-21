def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

class StringProcessor:
    REVERSE_METHOD = staticmethod(reverse_string_decorator)

    def __init__(self, string_func):
        self.string_func = string_func

    @REVERSE_METHOD
    def get_processed(self):
        return self.string_func()

def sample_string_function():
    return "Alibaba Cloud"

if __name__ == '__main__':
    processor = StringProcessor(sample_string_function)
    print(processor.get_processed())