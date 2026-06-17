def status_generator():
    for i in range(1, 21):
        if i % 2 == 0:
            yield 'Even'
        else:
            yield 'Odd'
if __name__ == '__main__':
    generator = status_generator()
    results = list(generator)
    print(results)