if __name__ == '__main__':
    for a in (False, True):
        for b in (False, True):
            print(f"{a} -> {b}: {int(not a or b)}")