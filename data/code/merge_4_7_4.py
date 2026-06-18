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
    a_sample = 10
    b_sample = 20
    c_sample = 30
    result = a_sample + b_sample + c_sample
    print(result)
    pass