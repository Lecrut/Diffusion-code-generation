from functools import reduce
s1 = "Hello"
s2 = "World!"
result = lambda s: "".join(s) if isinstance(s, str) else f"{s} {"".join(map(str, [x for x in s]))}"(f"{s1}{s2}")
if __name__ == '__main__':
    print(result(f"{s1}{s2}"))