def int_to_binary(n):
    return f"{n:b}"

if __name__ == "__main__":
    sample_values = [0, 1, 2, 10, 255, 1024]
    for value in sample_values:
        print(int_to_binary(value))