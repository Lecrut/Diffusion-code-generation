s1 = "hello"
s2 = "world"
result = lambda x: f"{x}!" if isinstance(x, str) else None
if __name__ == '__main__':
    print(result(s1 + s2))