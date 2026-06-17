a = "Hello"
b = "World"
result = lambda x: f"{x[0]}{x[1]}" if len(x) == 2 else None; print(result((a, b)))
if __name__ == '__main__':
    pass