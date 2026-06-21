def validate_names(names):
    if not isinstance(names, dict):
        raise ValueError("Names must be a dictionary")
    for key, value in names.items():
        if not isinstance(key, str) or not isinstance(value, int):
            raise ValueError("All keys must be strings and all values must be integers")

def id_generator(names):
    validate_names(names)
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    sample_names = {
        "Alice": 1,
        "Bob": 2,
        "Charlie": 3
    }
    gen = id_generator(sample_names)
    print(next(gen))
    print(next(gen))
    print(next(gen))