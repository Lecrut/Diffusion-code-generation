def boolean_inverter(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean value")
    if value:
        return False
    return True

if __name__ == '__main__':
    print(boolean_inverter(True))
    print(boolean_inverter(False))