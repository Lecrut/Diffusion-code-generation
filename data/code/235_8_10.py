def generate_arrowhead(width=5):
    arrowhead = []
    for i in range(width):
        row = [' '] * width
        row[i] = '/'
        row[-i-1] = '\\'
        arrowhead.append(''.join(row))
    return '\n'.join(arrowhead)

if __name__ == '__main__':
    print(generate_arrowhead())