if __name__ == '__main__':
    for A in (False, True):
        for B in (False, True):
            print(f"A: {A}, B: {B}, A implies B: {'true' if not A or B else 'false'}")