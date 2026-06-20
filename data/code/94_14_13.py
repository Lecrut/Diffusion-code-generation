def any_truthy(sequence):
    return any(item for item in sequence)

if __name__ == '__main__':
    print(any_truthy([0, False, '', None]))
    print(any_truthy([0, False, 'hello', None]))