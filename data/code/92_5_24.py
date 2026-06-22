def negate_bools(iterable):
    result = []
    for item in iterable:
        if item is True:
            result.append(False)
        elif item is False:
            result.append(True)
        else:
            raise ValueError(f"Expected bool, got {type(item)}")
    return result

if __name__ == '__main__':
    values = [True, False, True, False]
    inverted = negate_bools(values)
    print(inverted)