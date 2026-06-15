def display_square(side):
    for i in range(side):
        print("=" * (side * 2))
        for j in range(side):
            if i == 0:
                print("|" + " " * side + "|")
            elif i == side - 1:
                print("|" + " " * side + "|")
            else:
                row = ["|"]
                for j in range(side):
                    if j == i:
                        row.append("*" * (side + 1))
                    else:
                        row.append(" " + "-")
                row.append("|")
                print("".join(row))
        print("=" * (side * 2))
if __name__ == '__main__':
    sample_side = 5
    display_square(sample_side)