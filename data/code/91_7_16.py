def get_negated_value(data):
    if len(data) != 1:
        raise ValueError("Input must contain exactly one element")
    val = data[0]
    if val is True:
        return False
    if val is False:
        return True
    raise ValueError("Element must be boolean")

if __name__ == '__main__':
    sample = [True]
    print(get_negated_value(sample))