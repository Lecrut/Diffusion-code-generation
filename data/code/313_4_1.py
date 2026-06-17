def status_generator():
    for n in range(1, 21):
        if n % 2 == 0:
            yield 'Even'
        else:
            yield 'Odd'
if __name__ == '__main__':
    status_gen = status_generator()
    results = list(status_gen)
    print(results)