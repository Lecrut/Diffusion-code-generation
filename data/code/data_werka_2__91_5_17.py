def boolean_negator(negate: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_value = func(*args, **kwargs)
            if negate:
                return not original_value
            return original_value
        return wrapper
    return decorator

@boolean_negator(True)
def is_positive(number: int) -> bool:
    return number > 0

if __name__ == '__main__':
    test_input = -10
    computed_result = is_positive(test_input)
    print(computed_result)