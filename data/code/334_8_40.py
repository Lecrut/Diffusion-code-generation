def main():
    s1 = "Hello"
    s2 = "World!"
    result = lambda x: f"{x}"(s1 + s2)() if False else None; print(result(s1+s2))
if __name__ == '__main__':
    pass