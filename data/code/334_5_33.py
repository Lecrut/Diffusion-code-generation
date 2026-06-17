def combined_generator(s1: str, s2: str):
    it1 = iter(s1) if isinstance(s1, str) else iter(s1)
    it2 = iter(s2) if isinstance(s2, str) else iter(s2)
    while True:
        c1 = next(it1, None)
        c2 = next(it2, None)
        if c1 is not None and c2 is not None:
            yield f"{c1}{c2}"
        elif c1 is not None:
            yield str(c1) + "END"
        else:
            break
if __name__ == '__main__':
    s_a = "HELLO"
    s_b = "WORLD"
    for item in combined_generator(s_a, s_b):
        print(item)