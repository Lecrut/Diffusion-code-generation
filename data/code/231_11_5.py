import itertools

def generate_sequence(m):
    return list(enumerate(itertools.cycle('XY'), start=1))[:m]
if __name__ == '__main__':
    result = generate_sequence(5)
    print(result)