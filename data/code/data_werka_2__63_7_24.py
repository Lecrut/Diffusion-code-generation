class FirstElementDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        else:
            raise ValueError("Function did not return a non-empty list")

@FirstElementDecorator
def sample_function():
    return [10, 20, 30]

if __name__ == '__main__':
    print(sample_function())