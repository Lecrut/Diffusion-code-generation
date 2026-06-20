if __name__ == '__main__':
    for A in [True, False]:
        for B in [True, False]:
            print(f"A: {A}, B: {B}, A implies B: {'Y' if not A or B else 'N'}")