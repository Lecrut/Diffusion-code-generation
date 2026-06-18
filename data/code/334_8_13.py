from functools import reduce
a = "Hello"
b = "World"
result = lambda x: "".join([x]) if not a else "".join(list(a) + list(b))
if __name__ == '__main__':
    print(result(lambda s, t: f"{s}{t}"))