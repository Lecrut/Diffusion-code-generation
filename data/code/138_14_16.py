if __name__ == '__main__':
    A = [True, False]
    B = [True, False]
    
    for a in A:
        for b in B:
            print(f"{a} -> {b}: {'T' if not a or b else 'F'}")