def id_generator():
    names = {
        "Alice": 1,
        "Bob": 2,
        "Charlie": 3,
        "David": 4,
        "Eve": 5
    }
    
    def validate_names(names):
        if not isinstance(names, dict):
            raise ValueError("Names must be a dictionary")
        for name, id in names.items():
            if not isinstance(name, str) or not isinstance(id, int):
                raise ValueError("Invalid key-value pair in names dictionary")
    
    validate_names(names)
    
    for name, id in names.items():
        yield (name, id)

if __name__ == '__main__':
    gen = id_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))