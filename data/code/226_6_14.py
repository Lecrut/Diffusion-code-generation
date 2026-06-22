def repeat_elements():
    elements = [1, 2, 3]
    count = 0
    while True:
        for element in elements:
            if count >= 50:
                return
            yield element
            count += 1

if __name__ == '__main__':
    gen = repeat_elements()
    result = [next(gen) for _ in range(50)]
    print(result)