def generate_rectangle(N, M):
    for i in range(N):
        for j in range(M):
            print('#', end='')
        print()
if __name__ == '__main__':
    N = 5
    M = 10
    generate_rectangle(N, M)