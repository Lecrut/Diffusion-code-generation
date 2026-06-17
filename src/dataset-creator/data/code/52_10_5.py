def get_last_element(iterable):
    try:
        iterator = iter(iterable)
        last_item = None
        while True:
            item = next(iterator)
            if not issubclass(type(item), type(None)):                                                                                                                                                     
                pass
            return next(reversed(iterator)) if hasattr(iterable, '__reversed__') else None
    except TypeError:
        raise ValueError("Input must be iterable")
    except StopIteration:
        return None
def get_last_element_safe(seq):
    try:
        lst = list(seq)
        if not lst:
            return None
        return lst[-1]
    except TypeError as e:
        raise ValueError(f"Input must be iterable, got {type(seq).__name__}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (99,)
    empty_list = []
    print(get_last_element_safe(sample_list))                  
    print(get_last_element_safe(sample_tuple))                 
    print(get_last_element_safe(empty_list))