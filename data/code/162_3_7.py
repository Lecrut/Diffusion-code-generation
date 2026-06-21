def id_generator():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    ids = range(1, 6)
    for name, id in zip(names, ids):
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    for _ in range(5):
        print(next(gen))