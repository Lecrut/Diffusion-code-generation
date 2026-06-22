fibs = [0, 1]
[fibs.append(fibs[-1] + fibs[-2]) for _ in range(13)]
if __name__ == '__main__':
    print(fibs[:15])