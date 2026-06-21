def check_nested_conditions(a, b, c):
    return (a and b) or (c and not b)

if __name__ == '__main__':
    sample_values = {
        "a": True,
        "b": False,
        "c": True
    }
    result = check_nested_conditions(**sample_values)
    print(result)