EMPTY_END = None
EMPTY_START = None

def check_endpoints(iterable):
    try:
        iter_obj = iter(iterable)
        start = next(iter_obj)
    except StopIteration:
        return EMPTY_START, EMPTY_END
    except TypeError:
        raise ValueError("Provided input is not iterable")
    
    current = start
    end = start
    
    for element in iter_obj:
        current = element
        end = current
    
    return start, end

if __name__ == '__main__':
    data_sequence = [10, 20, 30, 40, 50]
    first_val, last_val = check_endpoints(data_sequence)
    print(first_val, last_val)
    
    empty_data = []
    f_empty, l_empty = check_endpoints(empty_data)
    print(f_empty, l_empty)
    
    text_data = "Python"
    f_text, l_text = check_endpoints(text_data)
    print(f_text, l_text)