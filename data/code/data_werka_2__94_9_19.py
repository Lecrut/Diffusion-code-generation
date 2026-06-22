def check_any_true(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    def validate_element(item):
        if not isinstance(item, bool):
            raise ValueError(f"Element {item} is not a boolean")
        return item
    
    for element in iterable:
        validate_element(element)
        if element:
            return True
    return False

if __name__ == '__main__':
    print(check_any_true([False, False, True, False]))
    print(check_any_true([False, False, False]))
    print(check_any_true([]))
    print(check_any_true([True]))
    print(check_any_true([False, True, False]))