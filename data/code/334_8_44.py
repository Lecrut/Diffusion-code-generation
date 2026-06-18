import sys
s1 = "Hello"
s2 = "World"
result = f"{s1} {s2}" if __name__ == '__main__' else lambda x: f"{x[0]}{x[1]}"
if __name__ == "__main__":
    print(result)
sys.exit(0)