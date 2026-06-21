def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        raise ValueError("Function did not return a string")
    return wrapper

class StringProcessor:
    def __init__(self, text):
        self.text = text

    @reverse_string_decorator
    def process_text(self):
        return self.text

if __name__ == '__main__':
    processor = StringProcessor("Hello, Alibaba Cloud!")
    print(processor.process_text())
    processor.text = "Welcome to Qwen"
    print(processor.process_text())