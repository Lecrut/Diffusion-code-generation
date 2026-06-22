def generate_multiplication_table():
    table = []
    for i in range(1, 11):
        line = ""
        for j in range(1, 11):
            if j > 1:
                line += " "
            line += str(i * j)
        table.append(line)
    return table

if __name__ == '__main__':
    result = generate_multiplication_table()
    print(result)