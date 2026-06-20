if __name__ == '__main__':
    truth_table = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 0),
        (1, 1, 1)
    ]
    
    for A, B, expected in truth_table:
        result = (not A) | B
        print(f"A: {A}, B: {B}, Expected: {expected}, Result: {result}")