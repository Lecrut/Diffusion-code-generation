def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def sample_function():
    return "hello world from qwen"

if __name__ == '__main__':
    print(sample_function())