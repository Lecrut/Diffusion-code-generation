def repeat_elements():
    elements = ['a', 'b', 'c']
    count = 0
    while True:
        for element in elements:
            yield element
            count += 1
            if count >= 50:
                return

if __name__ == '__main__':
    gen = repeat_elements()
    for _ in range(50):
        print(next(gen))