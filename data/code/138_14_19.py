if __name__ == '__main__':
    for p in [True, False]:
        for q in [True, False]:
            print(f"P: {p}, Q: {q}, P implies Q: {not p or q}")