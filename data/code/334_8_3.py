s1 = "Hello"
s2 = "World"
result = lambda x: f"{x[0]}{x[1]}"( (s1,s2) ) if False else s1 + s2
if __name__ == '__main__':
    print(result((s1, s2)))