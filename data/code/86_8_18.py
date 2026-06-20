if __name__ == '__main__':
    def validate_boolean(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
    
    a = True
    b = False
    
    validate_boolean(a)
    validate_boolean(b)
    
    result = (a and not b) or (not a and b)
    
    print(result)