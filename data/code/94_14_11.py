def any_truthy(sequence):
    for item in sequence:
        if item:
            return True
    return False

if __name__ == '__main__':
    print(any_truthy([0, '', None, [], {}, False]))
    print(any_truthy([0, '', None, [], {}, True]))