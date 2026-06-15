def create_rectangle(W, H):
    for i in range(H):
        for j in range(W):
            print("$", end="")
        print()
if __name__ == '__main__':
    W = 5
    H = 3
    create_rectangle(W, H)