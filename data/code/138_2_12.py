import itertools

def truth_table(operator):
    inputs = list(itertools.product([False, True], repeat=2))
    results = [operator(a, b) for a, b in inputs]
    return dict(zip(inputs, results))

and_op = lambda x, y: x and y
or_op = lambda x, y: x or y
not_op = lambda x: not x
xor_op = lambda x, y: x != y
nor_op = lambda x, y: not (x or y)
nand_op = lambda x, y: not (x and y)

if __name__ == '__main__':
    print("AND:", truth_table(and_op))
    print("OR:", truth_table(or_op))
    print("NOT:", {k: not_op(v) for k, v in truth_table(not_op).items()})
    print("XOR:", truth_table(xor_op))
    print("NOR:", truth_table(nor_op))
    print("NAND:", truth_table(nand_op))