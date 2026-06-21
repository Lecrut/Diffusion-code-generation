def name_id_generator():
    names = {
        "John": 10,
        "Sarah": 20,
        "Michael": 30,
        "Emily": 40,
        "William": 50,
        "Olivia": 60,
        "James": 70,
        "Sophia": 80,
        "Alexander": 90,
        "Isabella": 100
    }
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    gen = name_id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))