def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

class StringReverser:
    def __init__(self, string_func):
        self.string_func = string_func

    @reverse_string_decorator
    def get_reversed(self):
        return self.string_func()

def sample_string_function():
    return "Alibaba Cloud"

if __name__ == '__main__':
    reverser = StringReverser(sample_string_function)
    print(reverser.get_reversed())