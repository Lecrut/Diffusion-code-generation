def print_truth_table(input_tuples):
    headers = ['P', 'Q', 'P or Q']
    table = [headers] + [[p, q, p or q] for p, q in input_tuples]
    max_widths = [max(len(str(row[i])) for row in table) for i in range(3)]
    format_string = '|'.join(f'{{:<{width}}}' for width in max_widths)
    print(format_string.format(*headers))
    print('-' * sum(max_widths))
    for row in table[1:]:
        print(format_string.format(*row))

if __name__ == '__main__':
    input_tuples = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(input_tuples)