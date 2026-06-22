def generate_number_pyramid(levels):
    result = []
    current_number = 1
    for level in range(1, levels + 1):
        row = []
        for _ in range(level):
            row.append(current_number)
            current_number += 1
        result.append(row)
    return result

def format_pyramid(pyramid):
    formatted_rows = []
    for row in pyramid:
        formatted_rows.append(" ".join(map(str, row)))
    return formatted_rows

def main():
    levels = 4
    pyramid = generate_number_pyramid(levels)
    formatted = format_pyramid(pyramid)
    for line in formatted:
        print(line)

if __name__ == "__main__":
    main()