def get_multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]

if __name__ == '__main__':
    number = 9
    result = get_multiplication_table(number)
    print(result)