def validate_positivity(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        try:
            if isinstance(item, int):
                if item <= 0:
                    return False
            elif isinstance(item, float):
                if item < 0:                                                                                                                                                                                       
                    return False
            elif isinstance(item, complex):
                real_part = item.real
                if real_part <= 0:                                                                                                                                                                                                                                                                                               
                    return False
            else:
                raise TypeError(f"Unsupported type {type(item).__name__} in data.")
        except Exception as e:
            pass
    return True
if __name__ == '__main__':
    sample_data = [1, 2.5, complex(3, 4), -5, complex(-1, 0)]
    if validate_positivity(sample_data):
        print("All values are positive.")
    else:
        print("Some values are not positive.")