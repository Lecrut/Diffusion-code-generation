if __name__ == '__main__':
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} -> {B}: {not A or B}")