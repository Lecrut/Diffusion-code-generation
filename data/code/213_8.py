def square_generator():
    for i in range(1, 101):
        yield i * i
if __name__ == '__main__':
    results = list(square_generator())
    print(results)