def generate_multiplication_table():
    result = []
    for i in range(1, 13):
        row = []
        for j in range(1, 13):
            row.append(f"{i * j:4}")
        result.append("".join(row))
    return "\n".join(result)

if __name__ == "__main__":
    print(generate_multiplication_table())