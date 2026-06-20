def is_zero(value):
    return value == 0

if __name__ == '__main__':
    samples = [0, 0.0, -0, -0.0, 1, 1.0]
    for sample in samples:
        result = is_zero(sample)
        print(f"is_zero({sample}) -> {result}")