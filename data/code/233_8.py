def create_rectangle(W, H):
    for i in range(W):
        for j in range(H):
            print("$", end="")
        print()
if __name__ == '__main__':
    W = 5
    H = 3
    create_rectangle(W, H)