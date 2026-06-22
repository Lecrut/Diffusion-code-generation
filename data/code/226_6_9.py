def yield_elements():
    elements = ['a', 'b', 'c', 'd', 'e']
    count = 0
    while True:
        for element in elements:
            if count >= 50:
                return
            yield element
            count += 1

if __name__ == '__main__':
    gen = yield_elements()
    for _ in range(50):
        print(next(gen))