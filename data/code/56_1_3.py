def generate_multiplication_table(max_number):
    result = []
    header = ""
    for j in range(1, max_number + 1):
        header += f"{j:^10}"
    result.append(header)
    for i in range(1, max_number + 1):
        row = f"{i:^10}"
        for j in range(1, max_number + 1):
            row += f"{i * j:^10}"
        result.append(row)
    return "\n".join(result)

if __name__ == '__main__':
    max_number = 12
    output = generate_multiplication_table(max_number)
    print(output)