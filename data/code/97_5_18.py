VAR_NAMES = ['A', 'B', 'C', 'D']
if __name__ == '__main__':
    table = []
    for v1 in [0, 1]:
        for v2 in [0, 1]:
            for v3 in [0, 1]:
                for v4 in [0, 1]:
                    table.append((v1, v2, v3, v4))
    for row in table:
        print(f'{VAR_NAMES[0]}: {row[0]}, {VAR_NAMES[1]}: {row[1]}, {VAR_NAMES[2]}: {row[2]}, {VAR_NAMES[3]}: {row[3]}')