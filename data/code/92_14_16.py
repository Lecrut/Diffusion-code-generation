def invert_truth(flag: bool) -> bool:
    if type(flag) is not bool:
        raise ValueError("Expected boolean type")
    return bool(1 - int(flag))

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))