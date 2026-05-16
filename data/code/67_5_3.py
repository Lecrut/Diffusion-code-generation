def sum_generator(a, b):
    yield a + b
if __name__ == '__main__':
    gen = sum_generator(5, 3)
    print(list(gen))