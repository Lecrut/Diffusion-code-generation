import sys
def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
if __name__ == '__main__':
    n = 5
    print_triangle(n)