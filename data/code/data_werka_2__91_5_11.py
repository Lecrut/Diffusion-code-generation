def boolean_negator(negate: bool):
    if not isinstance(negate, bool):
        raise ValueError("Input must be a boolean")
    def decorator(func):
        def wrapper(value: bool) -> bool:
            if not isinstance(value, bool):
                raise ValueError("Function argument must be a boolean")
            if negate:
                return not value
            return value
        return wrapper
    return decorator

@boolean_negator(True)
def invert_flag(state: bool) -> bool:
    return state

def main():
    initial_state = True
    inverted_result = invert_flag(initial_state)
    print(inverted_result)

if __name__ == '__main__':
    main()