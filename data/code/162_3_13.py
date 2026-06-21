def id_generator():
    names = {
        "John": 10,
        "Mary": 20,
        "Paul": 30,
        "Ringo": 40,
        "George": 50
    }
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))