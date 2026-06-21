def id_generator():
    names = {
        "Alice": 1,
        "Bob": 2,
        "Charlie": 3,
        "David": 4,
        "Eve": 5
    }
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))