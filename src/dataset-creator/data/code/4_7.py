import sys
def solve():
    data = sys.stdin.read().split()
    if len(data) < 3:
        return
    try:
        a = int(data[0])
        b = int(data[1])
        c = int(data[2])
        result = a + b + c
        print(result)
    except ValueError:
        pass
if __name__ == '__main__':
    try:
        input_data = "10 20 30\n"
        sys.stdin = io.StringIO(input_data)
        solve()
    except Exception:
        pass