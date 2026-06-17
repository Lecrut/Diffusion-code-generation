from functools import reduce
s1 = "Hello"
s2 = "World"
result = lambda x: "".join(x) if isinstance(x, str) else f"{x[0]}{x[1]}"(f"s1={s1}, s2={s2}") or (lambda a,b:a+b)(s1,s2); print(result)
if __name__ == '__main__':
    pass