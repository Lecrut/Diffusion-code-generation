if __name__ == '__main__':
    for A in [True, False]:
        for B in [True, False]:
            result = not A or B
            print(f"A: {A}, B: {B}, A implies B: {result}")