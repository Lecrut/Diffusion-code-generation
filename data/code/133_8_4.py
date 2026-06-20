def logical_generator():
    yield True
    yield False
    yield True

if __name__ == '__main__':
    for result in logical_generator():
        print(result)