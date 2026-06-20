AND_TABLE = {
    (True, True): True,
    (True, False): False,
    (False, True): False,
    (False, False): False
}

OR_TABLE = {
    (True, True): True,
    (True, False): True,
    (False, True): True,
    (False, False): False
}

XOR_TABLE = {
    (True, True): False,
    (True, False): True,
    (False, True): True,
    (False, False): False
}

if __name__ == '__main__':
    for inputs, table in zip([(True, True), (True, False), (False, True), (False, False)], [AND_TABLE, OR_TABLE, XOR_TABLE]):
        print(f"Input A: {inputs[0]}, Input B: {inputs[1]}")
        print(f"Truth Table for A AND B: {table[(inputs[0], inputs[1])]}")
        print(f"Truth Table for A OR B: {OR_TABLE[(inputs[0], inputs[1])]}")
        print(f"Truth Table for A XOR B: {XOR_TABLE[(inputs[0], inputs[1])]}\n")