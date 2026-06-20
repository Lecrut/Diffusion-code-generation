class NegateDecorator:
    @staticmethod
    def create(negate):
        if not isinstance(negate, bool):
            raise ValueError("The 'negate' parameter must be a boolean.")
        
        class Wrapper:
            @staticmethod
            def inner(func):
                def wrapper(*args, **kwargs):
                    return not func(*args, **kwargs)
                return wrapper
        
        return Wrapper.inner

if __name__ == '__main__':
    sample_value = True
    negated_value = NegateDecorator.create(sample_value)(lambda: sample_value)()
    print(negated_value)