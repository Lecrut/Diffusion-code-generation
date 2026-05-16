if __name__ == '__main__':
    inputs = ['0', '1']
    print("Truth Table for A, B, C, D")
    for a in inputs:
        for b in inputs:
            for c in inputs:
                for d in inputs:
                    print(f"{a}{b}{c}{d}")