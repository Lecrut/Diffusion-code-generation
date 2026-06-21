def boolean_negator(flag: bool):
    NEGATE_MAP = {True: lambda x: not x, False: lambda x: x}
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            if not isinstance(original_result, bool):
                return original_result
            transformation = NEGATE_MAP.get(flag, lambda x: x)
            return transformation(original_result)
        return wrapper
    return decorator

@boolean_negator(True)
def evaluate_condition(value: int) -> bool:
    return value > 10

if __name__ == '__main__':
    sample_input = 5
    computed_result = evaluate_condition(sample_input)
    print(computed_result)