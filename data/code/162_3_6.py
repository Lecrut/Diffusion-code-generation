def id_generator():
    names = {
        "Zoe": 1,
        "Xander": 2,
        "Willow": 3,
        "Oliver": 4,
        "Nina": 5
    }
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))