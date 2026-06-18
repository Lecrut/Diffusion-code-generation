def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x: f"{x[0]}{x[1]}"(s1, s2) if __name__ == '__main__' else None or (lambda a,b:a+b)(s1,s2)
if __name__ == '__main__':
    print((lambda a,b:a+b)("Hello","World"))