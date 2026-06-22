def repeat_elements():
    elements = [1, 2, 3, 4, 5]
    count = 0
    while True:
        for element in elements:
            if count >= 50:
                return
            yield element
            count += 1

if __name__ == '__main__':
    gen = repeat_elements()
    for _ in range(50):
        print(next(gen))