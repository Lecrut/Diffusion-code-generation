def generate_multiplication_table():
    number = 7
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_multiplication_table())