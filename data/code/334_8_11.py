s1 = "Hello"
s2 = "World!"
result = lambda x: f"{x} {f'{s1}{s2}'}" if __name__ == '__main__' else None; print(result(s1 + s2))
if __name__ == "__main__":
    combined = (lambda a, b: a + " " + b)(s1, s2)
    print(combined)