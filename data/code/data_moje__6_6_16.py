lambda w1, w2: w1 - w2
if __name__ == '__main__':
    w1, w2 = 10, 5
    diff = (lambda w1, w2: w1 - w2)(w1, w2)
    print(diff)