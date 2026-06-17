import sys
def print_square(N):
    for i in range(N):
        for j in range(N):
            print("*", end="")
        print()
if __name__ == '__main__':
    print_square(3)
    print("\n")
    print_square(5)