def ml_to_lit(ml):
    try:
        return ml / 1000.0
    except OverflowError:
        return float('inf')

if __name__ == '__main__':
    print(ml_to_lit(500))