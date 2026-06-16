def is_odd(number: int) -> bool:
    return isinstance(number, int) and (number & 1) == 1
if __name__ == '__main__':
    sample_values = [-5, -2, 0, 3, 7, 16]
    for num in sample_values:
        if is_odd(num):
            print(f"{num} is odd")