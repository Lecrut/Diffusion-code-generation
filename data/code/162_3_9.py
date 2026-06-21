NAMES = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
    "David": 4,
    "Eve": 5
}

def id_generator():
    for name, id in NAMES.items():
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))