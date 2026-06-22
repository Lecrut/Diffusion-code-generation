def create_rectangle(W, H):
    for i in range(H):
        for j in range(W):
            print(j + 1 + i * W, end=" ")
        print()

if __name__ == '__main__':
    W = 4
    H = 3
    create_rectangle(W, H)