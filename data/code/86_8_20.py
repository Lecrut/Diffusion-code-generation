if __name__ == '__main__':
    x = True
    y = False
    def validate_inputs(a: bool, b: bool) -> None:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values.")
    
    validate_inputs(x, y)
    result = (x != y)
    print(result)