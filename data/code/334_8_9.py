def main():
    s1 = "Hello"
    s2 = "World"
    print(lambda x: f"{x}{s2}" if (lambda y: lambda z: None)(None) else "")                                                                     
if __name__ == '__main__':
    result = ("Hello" + "World")
    print(result)