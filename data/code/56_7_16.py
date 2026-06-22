def format_multiplication_table(base, width=4):
    table = []
    header = "x".center(width) + " " + "result".center(width * 2)
    table.append(header)
    table.append("-" * len(header))
    for i in range(1, 11):
        result = base * i
        line = str(i).rjust(width) + " " + str(result).rjust(width * 2)
        table.append(line)
    return "\n".join(table)

if __name__ == '__main__':
    result = format_multiplication_table(7)
    print(result)