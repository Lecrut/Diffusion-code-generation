import sys
def print_star_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
            if (j + 1) % n == 0:
                print()
        print()
if __name__ == '__main__':
    print_star_pattern(5)
    print("\n")
    print_star_pattern(3)