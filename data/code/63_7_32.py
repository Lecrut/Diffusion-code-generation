class FirstElementDecorator:
    @staticmethod
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and len(result) > 0:
                return result[0]
            else:
                raise ValueError("Function did not return a non-empty list")
        return inner

@FirstElementDecorator.wrapper
def sample_function():
    return [10, 20, 30]

if __name__ == '__main__':
    print(sample_function())