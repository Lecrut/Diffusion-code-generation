def generate_multiplication_rows(base, count):
    for i in range(1, count + 1):
        print(f"{base} x {i} = {base * i}")

if __name__ == '__main__':
    generate_multiplication_rows(9, 10)