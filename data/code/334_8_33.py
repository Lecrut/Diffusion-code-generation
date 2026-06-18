a = "Hello"
b = "World"
result = lambda s1, s2: f"{s1}{s2}"() if False else None; print(result(a, b))
if __name__ == '__main__':
    pass