def id_generator():
    yield ('Alice', 1)
    yield ('Bob', 2)
    yield ('Charlie', 3)

if __name__ == '__main__':
    for name, id in id_generator():
        print(f'{name}: {id}')