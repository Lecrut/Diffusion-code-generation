import sys
def generate_line_pattern(N):
    for i in range(1, N + 1):
        for j in range(i):
            print("*", end="")
        print()
if __name__ == '__main__':
    generate_line_pattern(5)