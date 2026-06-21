def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        raise ValueError("Function did not return a string")
    return wrapper

class StringProcessor:
    REVERSE_METHOD = staticmethod(reverse_string_decorator)

    @REVERSE_METHOD
    def get_processed_string(self):
        return "Hello, Alibaba Cloud!"

if __name__ == '__main__':
    processor = StringProcessor()
    print(processor.get_processed_string())