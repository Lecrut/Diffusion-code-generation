def invert_truth(value):
    if type(value) is not bool:
        raise ValueError("Argument must be of type bool")
    if value:
        return False
    return True

if __name__ == '__main__':
    results = [
        invert_truth(True),
        invert_truth(False)
    ]
    for res in results:
        print(res)